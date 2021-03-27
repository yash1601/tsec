from django.contrib import admin
from django.urls import path
from jobs import views

urlpatterns = [
    path("",views.index,name='jobs'),
    path("dashboard/",views.dashboard,name='dashboard'),
    path("login/", views.loginpage, name='login'),
    path("register/", views.register, name='register')
]
