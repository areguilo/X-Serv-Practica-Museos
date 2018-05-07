from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Museum, Comment, User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.template.loader import get_template
from django.template import Context

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

def mainPage(request):
    list = Museum.objects.all()
    response = '<ul><h2>'
    for item in list:
        response = response + '<li><a href=http://localhost:8000/' + str(item.name) + ">" + item.name + '</a></li>'
    response = response + '</ul></h2>'
    response = "<h1>Hoteles: </h1>" + response
    if request.user.is_authenticated():
        response += '<h2>Hi ' + request.user.username + ': <a href=http://localhost:8000/logout>logout</a></h2>'
    else:
        response += '<h2>Hi unknown client. Please <a href=http://localhost:8000/authenticate>login</a></h2>'
    return HttpResponse(response)

@csrf_exempt
def contentPage(request, name):
    changeContentForm = """<html><body><form action="" method = "POST"><br>
    <input type="text" name='content' value=""><br>
    <input type="submit"value="change content"></form></body></html>"""
    if request.method == "GET":
        try:
            object = Museum.objects.get(name = name)
            response = "<h2>The page's content is: </h2>" + object.page + '<br><br><a href=http://localhost:8000/> Return to Main menu </a><br><br>'
        except Museum.DoesNotExist:
            response = "There are not Museum for this object<br><a href=http://localhost:8000/> Return to Main menu </a><br>"
            return HttpResponse(response)
        if request.user.is_authenticated():
            response += '<h3>Change content:</h3>' + changeContentForm
    else:
        object = Museum.objects.get(name = name)
        object.page = request.POST['content']
        object.save()
        response = 'Actualised page<br><a href=http://localhost:8000/> Return to Main menu </a><br> \
        <a href=http://localhost:8000/' + name + '> Go to ' + name + "'s page </a>"
    return HttpResponse(response)

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
