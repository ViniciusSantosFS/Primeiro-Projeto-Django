
from django.contrib import admin
from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^list/', person_list, name= 'person_list'),
    url(r'^create/', person_create, name='person_create'),
    url(r'^edit/(?P<pk>[0-9]+)',person_edit ,name = 'person_edit'),
    url(r'^person_remove/(?P<pk>[0-9]+)',person_remove ,name = 'person_remove'),
    ]