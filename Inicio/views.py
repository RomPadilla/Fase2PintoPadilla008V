from django.shortcuts import render, HttpResponse

# Create your views here.

def Inicio(request):
    return render(
        request,
        'Inicio.html',
    )

def Naruto(request):
    return render(
        request,
        'Naruto.html',
    )
