from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', 'museos.views.mainPage'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', 'museos.views.loginView'),
	url(r'^logout', 'museos.views.logoutView'),
    url(r'^about', 'museos.views.about'),
    url(r'^museums/(\-?\d+)', 'museos.views.museumPage'),
    url(r'^museums', 'museos.views.museumsPage'),
    url(r'^(.*)/xml', 'museos.views.xmlUserPage'),
    url(r'^xml', 'museos.views.xmlMainPage'),
    url(r'^(.*)/json', 'museos.views.jsonUserPage'),
    url(r'^json', 'museos.views.jsonMainPage'),
    url(r'^(.*)', 'museos.views.personalPage'),
)
