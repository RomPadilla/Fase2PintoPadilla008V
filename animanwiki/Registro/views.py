from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Usuario
from django.views import generic

# Create your views here.

class UsuarioListView(generic.ListView):
    model = Usuario
    template_name='Usuarios.html'
    context_object_name='Usuarios'

class UsuarioCreate(CreateView):
    model=Usuario
    fields='__all__'
    
    
class UsuarioUpdate(UpdateView):
    model=Usuario
    fields=['Correo','Numero','Password']

class UsuarioDelete(DeleteView):
    model=Usuario
    success_url=reverse_lazy('usuario_create')

from django.views import generic

class UsuarioDetailView(generic.DetailView):
    model=Usuario
    


