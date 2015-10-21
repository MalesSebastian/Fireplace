from django.conf.urls import include, url
from django.contrib import admin
from . import views
from authen.views import *

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
]
