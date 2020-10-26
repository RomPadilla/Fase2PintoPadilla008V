from django.shortcuts import render
from .models import Personaje

# Create your views here.
def index(request):
    num_personaje=Personaje.objects.count()

    return render(
        request,
        'index.html',
        context={'num_personaje':num_personaje},
    )
