from django.db import models
from django.urls import reverse

# Create your models here.
class Usuario(models.Model):
    Nombre = models.CharField(max_length=16,help_text="Ingrese su nombre")
    Apellido = models.CharField(max_length=16,help_text="Ingrese su apellido")
    Correo = models.EmailField(max_length=60)
    Fecha = models.DateField()
    Numero = models.CharField(max_length=12,help_text="+56912345678")
    Username = models.CharField(max_length=16,help_text="Ingrese nombre de usuario")
    Password = models.CharField(max_length=16,help_text="Ingrese su contraseña")
    pers=(("1",'Naruto'),("2",'Sasuke'),("3",'Gaara'),("4",'Itachi'),("5",'Kakashi'),("6",'Sakura'),("7",'Otro'))
    Personaje= models.CharField(max_length=16, help_text="Seleccione su personaje favorito", choices=pers)

    def get_absolute_url(self):
        return reverse('usuario-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.Nombre} {self.Apellido} {self.Username}'
