# Generated by Django 3.1.2 on 2020-10-25 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ListaPersonajes', '0003_auto_20201025_1723'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='Personaje',
        ),
    ]
