from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'museos.views.mainPage'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', 'museos.views.loginView'),
	url(r'^logout', 'museos.views.logoutView'),
    #url(r'^authenticate', 'museos.views.loginPost'),
    url(r'^about', 'museos.views.about'),
    url(r'^museums/(\-?\d+)', 'museos.views.museumPage'),
    url(r'^museums', 'museos.views.museumsPage'),
    #url(r'^accessible', 'museos.views.accesiblePage'),
    #url(r'^static(.+)$'),
    url(r'^(.*)', 'museos.views.personalPage'),
)
