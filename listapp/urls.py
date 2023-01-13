from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.AllaListor.as_view(), name='listor-hem'),
    path('registrera/', views.registrera, name='registrera'),
    path('loggain/',auth_views.LoginView.as_view(template_name='listapp/loggain.html'),name='loggain'),
    path('loggaut/',auth_views.LogoutView.as_view(),name='loggaut'),
]