from django.db import models
from django.utils import timezone
# Create your models here.

class Museum(models.Model):
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    province = models.TextField()
    postal_code = models.TextField()
    tlfn = models.IntegerField()
    fax = models.CharField(max_length=32)
    mail = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=32)
    museum = models.ManyToManyField(Museum)
    color = models.CharField(max_length=16)
    background= models.CharField(max_length=32)
    title= models.CharField(max_length=32)
    size = models.IntegerField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User)
    museum = models.ForeignKey(Museum)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
