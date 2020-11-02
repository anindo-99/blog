from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('about/', views.about, name='about'),
    
    path('contact/', views.contact, name='contact'),
    path('upload/',views.upload,name='upload'),
    path('search/',views.search,name='search'),
    path('signup',views.handleSignup,name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('profile', views.profile, name='profile'),
    path('editprofile', views.editprofile, name='editprofile'),
    path('handleEditProfile', views.handleEditProfile, name='handleEditProfile'),
    path('logout', views.handleLogout, name='handleLogout'),
]
