# Generated by Django 4.1.3 on 2022-12-01 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppJuegos', '0003_carta_delete_estudiante'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carta',
            old_name='nombre',
            new_name='Nombrejuego',
        ),
        migrations.RenameField(
            model_name='carta',
            old_name='rareza',
            new_name='Rareza',
        ),
        migrations.RenameField(
            model_name='juegosdecartas',
            old_name='nombre_carta',
            new_name='Nombrecarta',
        ),
        migrations.RenameField(
            model_name='juegosdecartas',
            old_name='nombre_juego',
            new_name='Nombrejuego',
        ),
        migrations.RenameField(
            model_name='juegosdecartas',
            old_name='rareza',
            new_name='Rareza',
        ),
    ]
