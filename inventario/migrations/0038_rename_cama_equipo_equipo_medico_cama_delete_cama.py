# Generated by Django 4.2.4 on 2023-08-22 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0037_rename_cama_equipo_medico_cama_equipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipo_medico',
            old_name='cama_equipo',
            new_name='cama',
        )
    ]