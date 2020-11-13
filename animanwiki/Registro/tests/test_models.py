from django.test import TestCase
from Registro.models import Usuario
from django.core.files.uploadedfile import SimpleUploadedFile
import datetime



class UsuarioModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Usuario.objects.create(Nombre='Naruto', Apellido='Uzumaki', Correo='naruto@uzumaki.com',Fecha=datetime.date.today(),Numero="+56912345678" ,Username='hola', Password='hola', Personaje='Naruto')

    def test_Nombre_label(self):
        usuario=Usuario.objects.get(id=1)
        field_label = usuario._meta.get_field('Nombre').verbose_name
        self.assertEquals(field_label,'Nombre')

    def test_Apellido_label(self):
        usuario=Usuario.objects.get(id=1)
        field_label = usuario._meta.get_field('Apellido').verbose_name
        self.assertEquals(field_label,'Apellido')

    def test_Username_label(self):
        usuario=Usuario.objects.get(id=1)
        field_label = usuario._meta.get_field('Username').verbose_name
        self.assertEquals(field_label,'Username')


    def test_Nombre_max_length(self):
        usuario=Usuario.objects.get(id=1)
        max_length = usuario._meta.get_field('Nombre').max_length
        self.assertEquals(max_length,16)

    def test_Apellido_max_length(self):
        usuario=Usuario.objects.get(id=1)
        max_length = usuario._meta.get_field('Apellido').max_length
        self.assertEquals(max_length,16)

    def test_object_name_is_last_name_comma_first_name(self):
        usuario=Usuario.objects.get(id=1)
        expected_object_name = '%s, %s, %s' % (usuario.Nombre, usuario.Apellido, usuario.Username)
        self.assertEquals(expected_object_name,str(usuario))
