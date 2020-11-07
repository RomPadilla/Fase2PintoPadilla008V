from django.shortcuts import render
from .models import Informacione
from django.views import generic
# Create your views here.

class InformacioneListView(generic.ListView):
    model = Informacione
    template_name='Naruto.html'
    context_object_name='Informacione_list'
        
