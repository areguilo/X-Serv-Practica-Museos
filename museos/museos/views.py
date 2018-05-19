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
    in_order_0_5 = in_order[0:5]
    return in_order, in_order_0_5

def Adress (object):
    adress = object.NOMBRE_VIA + ", " + object.NUM + ", " + object.LOCALIDAD+ ", "+ object.PROVINCIA + ", " + object.CODIGO_POSTAL+ ", " + object.BARRIO + ", "+ object.DISTRITO
    return adress

def printMainPageMuseums(museums_to_print, string):
    museums = Museum.objects.all()
    for museum in museums_to_print:
        object = museums.get(NOMBRE=museum[0])
        link = object.CONTENT_URL
        museum_name = object.NOMBRE
        adress = Adress(object)
        museum_id = object.id
        string += '<li><a href=' + link +'>' + museum_name + '</a>'
        string += '<h4><strong> Adress: </strong>'+ adress + '</h4>'
        string += '<h8><a href=http://localhost:8000/museums/'+ str(museum_id) +'>more info</a></h8><br><br>'
    string += '</ul></li>'
    return string

def accessibles (request, museums):
    if (request.method == 'POST'):
        metodo = "GET"
        aviso = str(request.POST['button'])
        if aviso == "change_accessibles":
            all_museums = museums.filter(ACCESIBILIDAD=1)
    else:
        metodo = "POST"
        all_museums = museums
    return all_museums, metodo

def TitleUserPage (user):
    try:
        user_preference = Preference.objects.get(user=user)
        title = user_preference.title
        default_name = False
    except Preference.DoesNotExist:
        default_name = True
        title =  "<strong>" + user.username + "`s Page:</strong>"
    return title, default_name

def userPages():
    users = User.objects.all()
    list='<h4><strong>User`s pages available: </strong></h4><br><ul>'
    for user in users:
        title, default_name = TitleUserPage(user)
        list += '<li><h8><strong>' + user.username + '</strong>: <a href=http://localhost:8000/'+ str(user.id) +'>' + title + '</a></h8><br></li>'
    list += '</ul>'
    return list

@csrf_exempt
def mainPage(request):
    #boton sacado de https://www.aprenderaprogramar.co/home/alumnos/areguilo/pfinal1/X-Serv-Practica-Museos/museos',
    museums = Museum.objects.all()
    if museums.count() == 0:
        xmlparser()
        museums = Museum.objects.all()
    [all_museums, metodo] = accessibles(request, museums)
    username = request.user.username
    museums_in_order, museums_in_order_0_5 = museumsInOrder(all_museums)
    template = get_template('mainpage.html')
    if request.user.is_authenticated():
        auth = True
        response = '<h2>Hi ' + username
    else:
        auth = False
        response = ('<h2>Hi unknown client.</h2>')
    response += '<ul>'
    response = printMainPageMuseums(museums_in_order_0_5, response)
    pagperdis = userPages()
    return HttpResponse(template.render(Context({'response':response, 'metodo':metodo, 'auth':auth, 'pagperdis':pagperdis})))

def distrito_filter():
    museums = Museum.objects.all()
    distritos=[]
    for museum in museums:
        distritos.append(museum.DISTRITO)
    #http://blog.elcodiguero.com/python/eliminar-objetos-repetidos-de-una-lista.html
    lista=[]
    for i in distritos:
        if i not in lista:
            lista.append(i)
    DistritoForm = '''<form action="" Method="POST" id="respuesta">
                    <input type="submit" value="Enviar">
                    </form>
                    <select name="distrito" form="respuesta">
                    <option value=TODOS>TODOS</option>'''
    for distrito in lista:
        DistritoForm += '<option value="' + distrito + '">' + distrito + '</option>'
    DistritoForm +=  '</select>'
    print (DistritoForm)
    return DistritoForm

@csrf_exempt
def museumsPage(request):
    if request.user.is_authenticated():
        auth = True
    else:
        auth = False
    if request.method == 'GET':
        all_museums = Museum.objects.all()
    else:
        distrito = request.POST["distrito"]
        if distrito != "TODOS":
            print(distrito)
            all_museums = Museum.objects.filter(DISTRITO=distrito)
        else:
            all_museums = Museum.objects.all()
    response = "<h2>"
    museums_in_order, museums_in_order_0_5 = museumsInOrder(all_museums)
    response = printMainPageMuseums(museums_in_order, response)
    template = get_template('museumspage.html')
    response = distrito_filter() + response

    return HttpResponse(template.render(Context({'response':response, 'auth':auth})))

def nextPage(user,response,pagina):
    selecciones = UserMuseum.objects.filter(user=user)
    paginas = len(selecciones)

    if pagina == 0 and paginas>5:
        response += '<br><a href="?'+ str(pagina+1)+'">Next</a>'
    elif pagina == 0 and paginas <5:
        pass
    elif pagina < (paginas/5)-1:
        response += '<br><a href="?'+ str(pagina+1)+'">Next</a>'
        response += '<br><a href="?'+ str(pagina-1)+'">Previous</a>'
    else:
        response += '<br><a href="?'+ str(pagina-1)+'">Previous</a>'
    return response

@csrf_exempt
def personalPage(request, identifier):
    #######################################
    if request.user.is_authenticated():
        auth = True
    else:
        auth = False
    user = User.objects.get(id=identifier)
    user_museums = UserMuseum.objects.filter(user=user)
    title, default_name = TitleUserPage(user)
    ###########################################
    if default_name == True and request.user == user:
        NamePageForm = ("""<html><body><form action="" method = "POST"><br>
            Change Personal`s Name Page:<br>
            <input type="text" name='name' value=""><br>
            <input type="submit"value="send"></form></body></html>""")
        response = NamePageForm
    else:
        response=""
    if request.user == user:
        change_parametres = True
    else:
        change_parametres = False
    if request.method == "POST":
        #namepage = str(request.POST['name'])
        name= request.body.decode('utf-8').split("=")[0]
        if name == 'name':
            try:
                pref_user = Preference.objects.get(user=user)
                namepage = str(request.POST['name'])
                pref_user.title = namepage
            except Preference.DoesNotExist:
                pref_user = Preference(user=user, title=namepage)
            pref_user.save()
            return HttpResponseRedirect("/"+ str(user.id))
        elif name == 'Size':
            try:
                pref_user = Preference.objects.get(user=user)
                size = str(request.POST['Size'])
                pref_user.size = size
            except Preference.DoesNotExist:
                pref_user = Preference(user=user, size=size)
            pref_user.save()
            return HttpResponseRedirect("/"+ str(user.id))
        elif name == 'Color':
            try:
                pref_user = Preference.objects.get(user=user)
                color = str(request.POST['Color'])
                pref_user.background = color
            except Preference.DoesNotExist:
                pref_user = Preference(user=user, background=color)
            pref_user.save()
            return HttpResponseRedirect("/"+ str(user.id))

    ###########################################
    pagina = request.GET.urlencode().split('=')[0]
    if pagina == "":
        pagina = 0
    else:
        pagina = int(pagina)
    preferenciasmostrar = user_museums[5*pagina:5*(pagina+1)]
    ###########################################
    response += title + '<ul><h2>'
    for preference in preferenciasmostrar:
        fav_museum = Museum.objects.get(NOMBRE=preference.museums)
        museum_name = fav_museum.NOMBRE
        url = fav_museum.CONTENT_URL
        email = fav_museum.EMAIL
        tlfn = fav_museum.TELEFONO
        adress = Adress(fav_museum)
        date = str(preference.date).split(".")[0]
        response += '<li><a href=' + url + '>' + museum_name + '</a></li>'
        response += '<strong>-Adress: </strong>'+ adress + '<br>' + '<strong>-Like date: </strong>' + date + '<br>'
        response += '<strong>-Email: </strong>'+ email + '<br>' + '<strong>-Tlfn: </strong>' + tlfn + '<br>'
        response += '<a href=http://localhost:8000/museums/'+ str(fav_museum.id) +'>more info</a><br><br>'
    response += '</ul></h2>'
    response = nextPage(user,response,pagina)
    template = get_template('user_template.html')
    #response += "<br><a href=http://localhost:8000/> Return to Main Page </a><br>"
    if change_parametres == False:
        return HttpResponse(template.render(Context({'response':response, 'auth':auth, 'change_parametres':change_parametres})))
    else:
        return HttpResponse(template.render(Context({'response':response, 'auth':auth, 'change_parametres':change_parametres, 'color':Preference.objects.get(user=user).background, 'size':Preference.objects.get(user=user).size})))
    #######################################

@csrf_exempt
def museumPage(request, identifier):
    if request.user.is_authenticated():
        auth = True
    else:
        auth = False
    user = request.user
    museum = Museum.objects.all().get(id=identifier)
    description = museum.DESCRIPCION
    email = museum.EMAIL
    tlfn = museum.TELEFONO
    fax = museum.FAX
    horary = museum.HORARIO
    adress = Adress(museum)

    if museum.ACCESIBILIDAD == "0":
        accessible = "No"
    else:
        accessible = "Yes"

    response = "<strong><h1>"+ museum.NOMBRE + ": </h1><br><br>"
    response += "Description: </strong><br>" + description + "<br><br>"
    response += "<strong> Accessible: </strong>" + accessible + "<br><br>"
    response += "<strong> Adress: </strong>" + adress + "<br><br>"
    response += "<strong> Horary: </strong>" + horary+ "<br><br>"
    response += "<strong> EMAIL: </strong>" + email + "<br><br>"
    response += "<strong> Contact Number: </strong>" + tlfn + "<br><br>"
    response += "<strong> FAX: </strong>" + fax + "<br><br>"
    if request.method == 'GET':
        #museum = Museum.objects.all().get(id=identifier)
        CommentForm = ("""<html><body><form action="" method = "POST"><br>
            Put a comment:<br>
            <input id="comment_box" type="text" name='comment' value="" class="comment_box"><br>
            <input type="submit"value="Send comment"></form></body></html>""")

        LikeButton = ("""<html><body><form method= "POST" action="">
            <input type="hidden" name="button" value="like">
            <input type="submit" value="Add to favourites"></form></body></html>""")

        comments = Comment.objects.filter(museum=museum)
        response += "<strong>Comments: </strong><br><br>"
        if len(comments) == 0:
            response += 'the are no comments to this museum, be the first to comment it!'
        else:
            for comment in comments:
                response += '<li><strong>Comment:"</strong>' + comment.text + '". <strong>Date: </strong>'+ str(comment.date).split(".")[0] + '</li><br>'

        response += CommentForm + LikeButton

    elif request.method == 'POST':
        if "comment" in request.POST:
            comment = str(request.POST['comment'])
            comment = Comment(text=comment, user=user, museum=museum)
            comment.save()
            response = "Your comment was correctly added. "
        else:
            like = UserMuseum(user=user, museums=museum)
            like.save()
            response = "Your like was saved. "
        response += "<br><a href=http://localhost:8000/> Return to Main Page </a><br><a href=http://localhost:8000/museums/" + str(museum.id) + "> Return to the Museum`s Page </a></h2>"
        #title = user_preference.title
    template = get_template('museumpage.html')
    return HttpResponse(template.render(Context({'response':response, 'auth':auth})))


def about(response):
    template = get_template('about.html')
    return HttpResponse(template.render())


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
