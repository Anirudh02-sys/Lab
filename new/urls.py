from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('room/<str:pk>/', views.room , name='room'),
    path('adminPage',views.adminPage,name='adminPage'),
    path('audPage',views.audPage,name='audPage'),
    path('subPage',views.subPage,name='subPage'),
]