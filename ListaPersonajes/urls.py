from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('ListaPersonajes/',views.ListaPersonajes,name='ListaPersonajes'),
    path('Naruto/',views.Naruto,name='Naruto'),
]
