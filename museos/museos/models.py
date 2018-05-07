from django.db import models

# Create your models here.

class Museum(models.Model):
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    province = models.TextField()
    postal_code = models.TextField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    text = models.TextField()
    user = models.TextField()
    museum = models.ForeignKey(Museum)
    #date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.text
