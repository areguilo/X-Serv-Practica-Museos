from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Museum, Comment, User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.template.loader import get_template
from django.template import Context
import operator
# Create your views here.

def templateView(request):

    template = get_template('index.html')
    if request.user.is_authenticated():
        user = request.user.username
        link =  '<a href=http://localhost:8000/logout>logout</a>'
    else:
        user = 'Unknown client'
        link = 'Please <a href=http://localhost:8000/authenticate>login</a>'

    return HttpResponse(template.render(Context({'user':user, 'link':link})))

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
    template = get_template('index.html')
    if request.user.is_authenticated():
        response = '<ul><h2>'
        for museum in museums_in_order:
            object = museums.get(name=museum[0])
            link = object.mail
            name = object.name
            adress = object.location
            response = response + '<li><a href=' + link + '>' + name + 'direccion: '+ adress +'</a></li>'
        response = response + '</ul></h2>'
        return HttpResponse(response)
    else:
        return HttpResponse('<h2>Hi unknown client. Please <a href=http://localhost:8000/authenticate>login</a></h2>')
#def userParametres():
    #title = User.
    #size
    #color
    #background

#def mainPage(request):
#    list = Museum.objects.all()
#    response = '<ul><h2>'
#    for item in list:
#        response = response + '<li><a href=http://localhost:8000/' + str(item.name) + ">" + item.name + '</a></li>'
#    response = response + '</ul></h2>'
#    response = "<h1>Hoteles: </h1>" + response
#    if request.user.is_authenticated():
#        response += '<h2>Hi ' + request.user.username + ': <a href=http://localhost:8000/logout>logout</a></h2>'
#    else:
#        response += '<h2>Hi unknown client. Please <a href=http://localhost:8000/authenticate>login</a></h2>'
#    return HttpResponse(response)
