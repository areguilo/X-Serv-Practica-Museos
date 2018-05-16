from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Museum, Comment, UserMuseum, Preference
from .parser import xmlparser
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
        list[museum.NOMBRE] = museum.comment_set.count()
    #ordenamos el diccionario por su clave: (https://www.lawebdelprogramador.com/foros/Python/1524506-solucionado-ordenar-un-diccionario-por-su-clave-o-valor-en-Python.html)
    in_order = sorted(list.items(),key = operator.itemgetter(1), reverse = True)
    return in_order

def printMainPageMuseums(museums, museums_to_print, string):
    #print (museums_to_print)
    for museum in museums_to_print:
        object = museums.get(NOMBRE=museum[0])
        link = object.CONTENT_URL
        museum_name = object.NOMBRE
        museum_id = object.id
        adress = object.NOMBRE_VIA + ", " + object.NUM + ", " + object.LOCALIDAD+ ", "+ object.PROVINCIA + ", " + object.CODIGO_POSTAL+ ", " + object.BARRIO + ", "+ object.DISTRITO
        string += '<li><a href=' + link +'>' + museum_name + '</a>'
        string += '<h4> Adress: '+ adress + '</h4>'
        string += '<h8><a href=http://localhost:8000/museos/'+ str(museum_id) +'>more info</a></h8><br><br>'
    string += '</ul></li>'
    return string

def accessibles (request, museos):
    if (request.method == 'POST'):
        metodo = "GET"
        aviso = str(request.POST['button'])
        if aviso == "change_accessibles":
            all_museums = museos.filter(ACCESIBILIDAD=1)
    else:
        metodo = "POST"
        all_museums = museos
    return all_museums, metodo

def TitleUserPage (user):
    try:
        user_preference = Preference.objects.get(user=user)
        title = user_preference.title
    except Preference.DoesNotExist:
        title = 'pagina de ' + user.username
    return title

def userPages():
    users = User.objects.all()
    list='Enlaces paginas disponibles: <br><ul>'
    #print(users)
    for user in users:
        title = TitleUserPage(user)
        list += '<li><strong>' + user.username + '</strong>: <a href=http://localhost:8000/'+ str(user.id) +'>' + title + '</a><br></li>'
    list += '</ul>'
    return list

@csrf_exempt
def mainPage(request):
    #boton sacado de https://www.aprenderaprogramar.co/home/alumnos/areguilo/pfinal1/X-Serv-Practica-Museos/museos',
    museums = Museum.objects.all()
    if museums.count() == 0:
        xmlparser()
        museums = Museum.objects,all
    print("1")
    [all_museums, metodo] = accessibles(request, museums)
    username = request.user.username
    print("2")
    museums_in_order = museumsInOrder(all_museums)
    template = get_template('mainpage.html')
    print("3")
    if request.user.is_authenticated():
        auth = True
        response = '<h2>Hi ' + username
        #response += ': <a href=http://localhost:8000/'+ username + '>Página de '+ username + '</a></h2>'
        #response += '<h2>Click here to <a href=http://localhost:8000/logout>logout</a></h2>'
    else:
        auth = False
        response = ('<h2>Hi unknown client.</h2>')
    response += '<ul>'
    response = printMainPageMuseums(all_museums, museums_in_order, response)
    pagperdis = userPages()
    return HttpResponse(template.render(Context({'response':response, 'metodo':metodo, 'auth':auth, 'pagperdis':pagperdis})))

@csrf_exempt
def personalPage(request, identifier):
    #######################################
    template = get_template('user_template.html')
    user = User.objects.get(id=identifier)
    user_preferences = UserMuseum.objects.filter(user=user)
    title = TitleUserPage(user)
    response= title + '<ul><h2>'
    for preference in user_preferences:
        fav_museum = Museum.objects.get(NOMBRE=preference.museums)
        museum_name = fav_museum.NOMBRE
        email = fav_museum.CONTENT_URL
        adress = "fav_museum.location"
        date = str(preference.date)
        response += '<li><a href=' + email + '>' + museum_name + '</a></li>'
        response += 'adress: '+ adress + '<br>' + 'fecha de like: ' + date + '<br>'
        response += '<a href=http://localhost:8000/museos/'+ str(fav_museum.id) +'>more info</a><br><br>'
    response += '</ul></h2>'
    return HttpResponse(template.render(Context({'response':response})))
    #######################################

def museumPage(request, identifier):
    museum = Museum.objects.all().get(id=identifier)
    description = museum.description
    response = description
    response += "<a href=http://localhost:8000/> Return to Main Page </a></h2>"
    return HttpResponse(response)

def about(response):
    #template = get_template('about.html')
    #return HttpResponse(template.render())
    a=parserXML()
    return HttpResponse(a)

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
