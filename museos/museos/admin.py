from django.contrib import admin

# Register your models here.

from museos.models import Museum, Comment, UserMuseum, Preference

admin.site.register(Museum)
admin.site.register(Comment)
admin.site.register(UserMuseum)
admin.site.register(Preference)
