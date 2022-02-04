from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='frontsite-home'),
    path('rooms', views.rooms, name='frontsite-rooms'),
    path('single-room/<str:pk_test>/', views.singleroom),
]


