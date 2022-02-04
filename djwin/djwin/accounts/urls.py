import imp
from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('home', home, name="home"),
    path('register', register_user, name="register_user"),
    path('login', login_user, name='login_user'),
    path('success', success, name='success'),
    path('token', token_send, name='token_send'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error' , error_page , name="error")
]