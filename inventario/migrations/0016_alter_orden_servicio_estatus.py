# Generated by Django 4.2.3 on 2023-07-26 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0015_alter_orden_servicio_autorizo_jefe_biomedica_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden_servicio',
            name='estatus',
            field=models.CharField(choices=[('FUN', 'Equipo funcional'), ('OUT', 'Equipo fuera de servicio'), ('N/A', 'No se realizo servicio'), ('PEN', 'Pendiente')], default='PEN', max_length=3),
        ),
    ]
