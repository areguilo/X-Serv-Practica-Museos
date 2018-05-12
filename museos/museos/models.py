from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Museum(models.Model):
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    province = models.TextField()
    postal_code = models.TextField()
    description = models.TextField()
    tlfn = models.IntegerField()
    fax = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    accessibility = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class UserMuseum(models.Model):
    user = models.ForeignKey(User, related_name="user") #nombre de la relacion inversa para volver de User a UserMuseum
    museums = models.OneToOneField(Museum)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

class Preference(models.Model):
    user = models.ForeignKey(User)
    title= models.CharField(max_length=32)
    size = models.IntegerField()
    color = models.CharField(max_length=16)
    background= models.CharField(max_length=32)

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(UserMuseum)
    museum = models.ForeignKey(Museum)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
