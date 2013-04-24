from django.conf.urls import patterns, url

from blogs import views

urlpatterns = patterns('',
    url(r'^$', views.entry_list, name='index'),
    url(r'^user/$', views.user_list, name='user_list'),
    url(r'^user/(?P<username>\w+)/$', views.entry_list, name='user_home'),
    url(r'^tag/$', views.tag_list, name='tag_list'),
    url(r'^tag/(?P<tag>\w+)/$', views.entry_list, name='tagged_entry_list'),
    url(r'^entry/create', views.create_entry, name='create_entry'),
    url(r'^entry/(?P<entry_id>\d+)/$', views.detail_entry, name='detail_entry'),
    url(r'^entry/(?P<entry_id>\d+)/edit/$', views.edit_entry, name='edit_entry'),
    url(r'^entry/(?P<entry_id>\d+)/update/$', views.update_entry, name='update_entry'),
    url(r'^entry/(?P<entry_id>\d+)/delete/$', views.delete_entry, name='delete_entry'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/', views.user_logout, name='logout'),
)
