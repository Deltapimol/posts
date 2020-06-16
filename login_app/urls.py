from django import urls
from django.urls import path, include
from .views import userRegister


urlpatterns = [
    
    path(r'^userRegister/$',userRegister,name='userRegister'),
       
]