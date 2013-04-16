from django.conf.urls import patterns, url
from django.views.generic import ListView
from django.forms.models import modelform_factory

from todos import views
from todos.models import Todo

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add/', views.add, name='add'),
    url(r'^(?P<todo_id>\d+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<todo_id>\d+)/update/$', views.update, name='update'),
    url(r'^(?P<todo_id>\d+)/close/$', views.close, name='close'),
)
