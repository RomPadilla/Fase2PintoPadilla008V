from django.urls import path
from . import views

urlpatterns=[
    path('',views.PersonajeListView.as_view(),name='ListaPersonajes'),
]
