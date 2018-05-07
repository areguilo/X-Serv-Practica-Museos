from django.contrib import admin

# Register your models here.

from museos.models import Museum, Comment, User

admin.site.register(Museum)
admin.site.register(Comment)
admin.site.register(User)
