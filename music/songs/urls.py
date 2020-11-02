from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.songhome, name='songhome'),
    path('songuserPost', views.songuserPost, name='songuserPost'),
    path('<str:slug>/', views.songPost, name='songPost'),
    

    

]
