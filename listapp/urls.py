from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.AllaListor.as_view(), name='listor-hem'),
    path('registrera/', views.registrera, name='registrera'),
]