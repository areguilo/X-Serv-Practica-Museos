import xml.etree.ElementTree as ET
from django.views.decorators.csrf import csrf_exempt
from .models import Museum


@csrf_exempt
def xmlparser():
    tree = ET.parse('museos/museos.xml')
    id_entidad =""
    nombre= ""
    descripcion_entidad= ""
    horario= ""
    transporte= ""
    descripcion= ""
    accesibilidad=""
    content_url= ""
    nombre_via= ""
    num= ""
    localidad= ""
    provincia= ""
    codigo_postal= ""
    barrio= ""
    distrito= ""
    X= ""
    Y= ""
    latitud= ""
    longitud= ""
    telefono= ""
    fax= ""
    email= ""
    tipo= ""
    #https://docs.python.org/2/library/xml.etree.elementtree.html
    root = tree.getroot()
    #print("1")
    for contenido in root.findall('contenido'):
        #print("2")
        for atributos in contenido.findall('atributos'):
            #print("3")
            for atributo in atributos.findall('atributo'):
                #print (atributo)
                if atributo.get ('nombre') == ("ID-ENTIDAD"):
                    id_entidad = atributo.text
                    #print(id_entidad)
                if atributo.get ('nombre') == ("NOMBRE"):
                    nombre = atributo.text;
                    #print (nombre)
                if atributo.get ('nombre') == ("DESCRIPCION-ENTIDAD"):
                    descripcion_entidad = atributo.text;
                if atributo.get ('nombre') == ("HORARIO"):
                    horario = atributo.text;
                if atributo.get ('nombre') == ("TRANSPORTE"):
                    transporte = atributo.text;
                if atributo.get ('nombre') == ("DESCRIPCION"):
                    descripcion = atributo.text;
                if atributo.get ('nombre') == ("ACCESIBILIDAD"):
                    accesibilidad = atributo.text;
                if atributo.get ('nombre') == ("CONTENT-URL"):
                    content_url = atributo.text;
                if atributo.get ('nombre') == ("LOCALIZACION"):
                    for atributo_2 in atributo.findall('atributo'):
                        if atributo_2.get ('nombre') == ("NOMBRE-VIA"):
                            nombre_via = atributo_2.text;
                        if atributo_2.get ('nombre') == ("NUM"):
                            num = atributo_2.text;
                        if atributo_2.get ('nombre') == ("LOCALIDAD"):
                            localidad = atributo_2.text;
                        if atributo_2.get ('nombre') == ("PROVINCIA"):
                            provincia = atributo_2.text;
                        if atributo_2.get ('nombre') == ("CODIGO-POSTAL"):
                            codigo_postal = atributo_2.text;
                        if atributo_2.get ('nombre') == ("BARRIO"):
                            barrio = atributo_2.text;
                        if atributo_2.get ('nombre') == ("DISTRITO"):
                            distrito = atributo_2.text;
                        if atributo_2.get ('nombre') == ("COORDENADA-X"):
                            X = atributo_2.text;
                        if atributo_2.get ('nombre') == ("COORDENADA-Y"):
                            Y = atributo_2.text;
                        if atributo_2.get ('nombre') == ("LATITUD"):
                            latitud = atributo_2.text;
                        if atributo_2.get ('nombre') == ("LONGITUD"):
                            longitud = atributo_2.text;
                if atributo.get ('nombre') == ("DATOSCONTACTOS"):
                    for atributo_2 in atributo.findall('atributo'):
                        if atributo_2.get ('nombre') == ("TELEFONO"):
                            telefono = atributo_2.text
                        if atributo_2.get ('nombre') == ("FAX"):
                            fax = atributo_2.text
                        if atributo_2.get ('nombre') == ("EMAIL"):
                            email = atributo_2.text
                if atributo.get ('nombre') == ("TIPO"):
                            tipo = atributo.text;

            museum = Museum (ID_ENTIDAD=id_entidad,NOMBRE=nombre,DESCRIPCION_ENTIDAD=descripcion_entidad, HORARIO=horario, TRANSPORTE=transporte, DESCRIPCION=descripcion,
    	ACCESIBILIDAD=accesibilidad, CONTENT_URL=content_url, NOMBRE_VIA=nombre_via, NUM=num, LOCALIDAD=localidad, PROVINCIA=provincia,
        CODIGO_POSTAL=codigo_postal, BARRIO=barrio,	DISTRITO=distrito, COORDENADA_X=X, COORDENADA_Y=Y, LATITUD=latitud, LONGITUD=longitud,
        TELEFONO=telefono, FAX=fax, EMAIL=email, TIPO=tipo)
            museum.save()
