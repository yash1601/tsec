from django.contrib import admin
from django.urls import path
from jobs import views

urlpatterns = [
    path("",views.index,name='jobs')
]
