from django.shortcuts import render
from .models import Personaje
from django.views import generic
class PersonajeListView(generic.ListView):
    model = Personaje
    template_name='ListaPersonajes.html'
    context_object_name='Personaje_list'
