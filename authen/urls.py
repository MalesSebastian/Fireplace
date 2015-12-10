from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.app_login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^index/', views.index, name='index'),
]
