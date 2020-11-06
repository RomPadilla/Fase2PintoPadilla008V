from django.shortcuts import render
from .models import Personaje

# Create your views here.


def ListaPersonajes(request):
    num_personaje=Personaje.objects.count()

    return render(
        request,
        'ListaPersonajes.html',
        context={'num_personaje':num_personaje},
    )

def Naruto(request):
    return render(
        request,
        'Naruto.html',
    )
