from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^todos/', include('todos.urls', namespace='todos')),
    url(r'^blogs/', include('blogs.urls', namespace='blogs')),
    url(r'^photos/', include('photos.urls', namespace='photos')),
    # Examples:
    # url(r'^$', 'myapps.views.home', name='home'),
    # url(r'^myapps/', include('myapps.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
