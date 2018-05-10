from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Museum, Comment, User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.template.loader import get_template
from django.template import Context
import operator
# Create your views here.

def museumsInOrder(museums):
    #print (museums)
    #print (museums[3].comment_set.count()) #me dice numero de comentarios que tiene el museo
    list = {}
    for museum in museums:
        list[museum.name] = museum.comment_set.count()
    #ordenamos el diccionario por su clave: (https://www.lawebdelprogramador.com/foros/Python/1524506-solucionado-ordenar-un-diccionario-por-su-clave-o-valor-en-Python.html)
    in_order = sorted(list.items(),key = operator.itemgetter(1), reverse = True)
    return in_order

def printMuseums(museums, museums_to_print, string):
    for museum in museums_to_print:
        object = museums.get(name=museum[0])
        link = object.email
        museum_name = object.name
        adress = object.location
        string += '<li><a href=' + link + '>' + museum_name + '</a></li>'
        string += 'adress: '+ adress + '<br>'
        string += '<a href=http://localhost:8000/'+ museum_name +'>more info</a><br><br>'
    string += '</ul></h2>'
    return string

def mainPage(request):
    username = request.user.username
    all_museums = Museum.objects.all()
    museums_in_order = museumsInOrder(all_museums)
    print (museums_in_order)
    template = get_template('mainpage.html')
    if request.user.is_authenticated():
        response = '<h2>Hi ' + username +  ': <a href=http://localhost:8000/'+ username + '>Página de '+ username + '</a></h2>'
        response += '<h2>Click here to <a href=http://localhost:8000/logout>logout</a></h2>'
        response += '<ul><h2>'
        response = printMuseums(all_museums, museums_in_order, response)
    else:
        response = ('<h2>Hi unknown client. Please <a href=http://localhost:8000/authenticate>login</a></h2>')
    return HttpResponse(template.render(Context({'response':response})))

def personalPage(request, name):
    user = User.objects.filter(name = name)
    username = str(user[0])
    all_museums = Museum.objects.all()
    user_museums = Museum.objects.filter(user=user)
    user_museums_in_order = museumsInOrder(user_museums)
    #print (all_museums)
    #print (user_museums)
    #print (user_museums_in_order)
    template = get_template('user_template.html')
    if request.user.is_authenticated():
        response = '<ul><h2>'
        response = printMuseums(all_museums, user_museums_in_order, response)
        response += "<br><a href=http://localhost:8000/> Return to Main Page </a><br>"
        return HttpResponse(template.render(Context({'response':response})))
    else:
        return HttpResponse('<h2>Hi unknown client. Please <a href=http://localhost:8000/authenticate>login</a></h2>')

#def museumsPage(request, name)

def about(response):
    return HttpResponse("p<a href=http://localhost:8000/> Return to Main Page </a></h2>")

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
