#from django.conf.urls import url
from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^$', views.todo_list, name='todo_list'),
    url(r'^todo/(?P<pk>[0-9]+)/$', views.todo_detail, name='todo_detail'),
    url(r'^todo/new/$', views.todo_new, name='todo_new'),
    url(r'^todo/(?P<pk>[0-9]+)/edit/$', views.todo_edit, name='todo_edit'),
    url(r'^type/new/$', views.type_new, name='type_new'),
    url(r'^type/(?P<pk>[0-9]+)/$', views.type_detail, name='type_detail'),
    url(r'^type/(?P<pk>[0-9]+)/edit/$', views.type_edit, name='type_edit'),
    url(r'^type$', views.type_list, name='type_list'),
]
