from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Museum, Comment, UserData
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.template.loader import get_template
from django.template import Context
import operator
# Create your views here.

def museumsInOrder(museums):
    list = {}
    for museum in museums:
        list[museum.name] = museum.comment_set.count()
    #ordenamos el diccionario por su clave: (https://www.lawebdelprogramador.com/foros/Python/1524506-solucionado-ordenar-un-diccionario-por-su-clave-o-valor-en-Python.html)
    in_order = sorted(list.items(),key = operator.itemgetter(1), reverse = True)
    return in_order

def printMainPageMuseums(museums, museums_to_print, string):
    print (museums_to_print)
    for museum in museums_to_print:
        object = museums.get(name=museum[0])
        link = object.email
        museum_name = object.name
        museum_id = object.id
        adress = object.location
        string += '<li><a href=' + link + '>' + museum_name + '</a></li>'
        string += 'adress: '+ adress + '<br>'
        string += '<a href=http://localhost:8000/museos/'+ str(museum_id) +'>more info</a><br><br>'
    string += '</ul></h2>'
    return string

def accessibles (request, museos):
    if (request.method == 'POST'):
        metodo = "GET"
        aviso = str(request.POST['button'])
        if aviso == "change_accessibles":
            all_museums = museos.filter(accessibility=True)
    else:
        metodo = "POST"
        all_museums = museos
    return all_museums, metodo

@csrf_exempt
def mainPage(request):
    #boton sacado de https://www.aprenderaprogramar.co/home/alumnos/areguilo/pfinal1/X-Serv-Practica-Museos/museos',
    museos = Museum.objects.all()
    [all_museums, metodo] = accessibles(request, museos)
    username = request.user.username
    museums_in_order = museumsInOrder(all_museums)
    template = get_template('mainpage.html')
    if request.user.is_authenticated():
        response = '<h2>Hi ' + username
        response += ': <a href=http://localhost:8000/'+ username + '>Página de '+ username + '</a></h2>'
        response += '<h2>Click here to <a href=http://localhost:8000/logout>logout</a></h2>'
        response += '<ul><h2>'
        response = printMainPageMuseums(all_museums, museums_in_order, response)
    else:
        response = ('<h2>Hi unknown client. Please <a href=http://localhost:8000/authenticate>login</a></h2>')
    return HttpResponse(template.render(Context({'response':response, 'metodo':metodo})))

@csrf_exempt
def personalPage(request, name):
    #######################################
    template = get_template('user_template.html')
    user = request.user
    user_preferences = UserData.objects.filter(user=user)
    response='<ul><h2>'
    for preference in user_preferences:
        fav_museum = Museum.objects.get(name=preference.museums)
        museum_name = fav_museum.name
        email = fav_museum.email
        adress = fav_museum.location
        date = str(preference.date)
        response += '<li><a href=' + email + '>' + museum_name + '</a></li>'
        response += 'adress: '+ adress + '<br>' + 'fecha de like: ' + date + '<br>'
        response += '<a href=http://localhost:8000/museos/'+ str(fav_museum.id) +'>more info</a><br><br>'
    response += '</ul></h2>'
    return HttpResponse(template.render(Context({'response':response})))
    #######################################

def museumPage(request, identifier):
    museum = Museum.objects.all().get(museum_id=identifier)
    description = museum.description
    response = description
    response += "<a href=http://localhost:8000/> Return to Main Page </a></h2>"
    return HttpResponse(response)

def about(response):
    template = get_template('about.html')
    return HttpResponse(template.render())

def loginPost(request):
    loginForm = ("""<html><body><form action="/login" method = "POST">
    Username:<br>
    <input type="text" name='username' value=""><br>
    Password:<br>
    <input type="password" name='password' value=""><br>
    <input type="submit"value="login"></form></body></html>""")
    return HttpResponse(loginForm)

@csrf_exempt
def loginView(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('http://localhost:8000/')
        else:
            response = 'Error: disables account <br><br><a href=http://localhost:8000/> Return to Main menu </a>'
    else:
        response = 'Error: invalid login <br><br><a href=http://localhost:8000/> Return to Main menu </a>'
    return HttpResponse(response)

def logoutView(request):
    logout(request)
    return HttpResponseRedirect('http://localhost:8000/')
