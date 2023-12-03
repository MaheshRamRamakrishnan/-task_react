from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [

    path('', views.home),
    # path('abc/', views.ind),
    path('login/', views.home2),
    path('Task_register/', views.T_register),
    path('Task_login/', views.T_login),
]
