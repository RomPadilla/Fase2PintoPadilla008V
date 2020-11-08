from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Usuario

# Create your views here.

class UsuarioCreate(CreateView):
    model=Usuario
    fields='__all__'
    
class UsuarioUpdate(UpdateView):
    model=Usuario
    fields=['Correo','Numero','Password','Avatar']

class UsuarioDelete(DeleteView):
    model=Usuario
    success_url=reverse_lazy('Registro')

from django.views import generic

class UsuarioDetailView(generic.DetailView):
    model=Usuario
