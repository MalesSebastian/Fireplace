from django.conf.urls import include, url
from django.contrib import admin
from . import views
from authen.views import *

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^index/' , views.index, name='index'),
    url(r'^index/' , views.index2, name='index2')
]
