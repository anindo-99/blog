from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.bloghome, name='bloghome'),
    path('blogupload',views.blogupload,name="blogupload"),
    path('bloguploaded', views.bloguploaded, name="bloguploaded"),
    path('<str:slug>/', views.blogPost, name='blogPost'),
    path('postComment',views.postComment,name="postComment"),
    
]
