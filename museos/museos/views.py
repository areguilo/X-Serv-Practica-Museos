from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Museum, Comment, User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.template.loader import get_template
from django.template import Context
import operator
# Create your views here.

def museumsInOrder():
    museums = Museum.objects.all()
    #print (museums)
    #print (museums[3].comment_set.count()) #me dice numero de comentarios que tiene el museo
    list = {}
    for museum in museums:
        list[museum.name] = museum.comment_set.count()
    #ordenamos el diccionario por su clave: (https://www.lawebdelprogramador.com/foros/Python/1524506-solucionado-ordenar-un-diccionario-por-su-clave-o-valor-en-Python.html)
    in_order = sorted(list.items(),key = operator.itemgetter(1), reverse = True)
    return in_order

def mainPage(request):
    museums = Museum.objects.all()
    museums_in_order = museumsInOrder()
    template = get_template('mainpage.html')
    if request.user.is_authenticated():
        response = '<h2>Hi ' + request.user.username +  ' <a href=http://localhost:8000/logout>logout</a></h2>'
        response += '<ul><h2>'
        for museum in museums_in_order:
            object = museums.get(name=museum[0])
            link = object.mail
            name = object.name
            adress = object.location
            response = response + '<li><a href=' + link + '>' + name + '</a></li>'
            response += 'adress: '+ adress + '<br>'
            response += 'aquí va el enlace<br><br>'
        response += '</ul></h2>'
        return HttpResponse(template.render(Context({'response':response})))
    else:
        return HttpResponse('<h2>Hi unknown client. Please <a href=http://localhost:8000/authenticate>login</a></h2>')
#def userParametres():
    #title = User.
    #size
    #color
    #background
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
