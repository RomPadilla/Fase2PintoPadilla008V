from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('',views.Inicio,name='Inicio'),
    path('ListaPersonajes/',include('ListaPersonajes.urls')),
    path('Naruto/',views.Naruto,name='Naruto'),  
]
