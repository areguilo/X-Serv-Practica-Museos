from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Museum(models.Model):
    ID_ENTIDAD = models.TextField()
    NOMBRE = models.TextField()
    DESCRIPCION_ENTIDAD = models.TextField()
    HORARIO = models.TextField()
    TRANSPORTE = models.TextField()
    DESCRIPCION = models.TextField()
    ACCESIBILIDAD = models.TextField()
    CONTENT_URL = models.TextField()
    NOMBRE_VIA = models.TextField()
    NUM = models.TextField()
    LOCALIDAD = models.TextField()
    PROVINCIA = models.TextField()
    CODIGO_POSTAL  = models.TextField()
    BARRIO = models.TextField()
    DISTRITO = models.TextField()
    COORDENADA_X  = models.TextField()
    COORDENADA_Y  = models.TextField()
    LATITUD = models.TextField()
    LONGITUD = models.TextField()
    TELEFONO = models.TextField()
    FAX = models.TextField()
    EMAIL = models.TextField()
    TIPO = models.TextField()

    def __str__(self):
        return self.NOMBRE

class UserMuseum(models.Model):
    user = models.ForeignKey(User, related_name="user") #nombre de la relacion inversa para volver de User a UserMuseum
    museums = models.ForeignKey(Museum)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

class Preference(models.Model):
    user = models.ForeignKey(User)
    title= models.CharField(max_length=32)
    size = models.CharField(max_length=3, default="9px")
    #color = models.CharField(max_length=16, default="black")
    background= models.CharField(max_length=32, default="green")

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User)
    museum = models.ForeignKey(Museum)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
