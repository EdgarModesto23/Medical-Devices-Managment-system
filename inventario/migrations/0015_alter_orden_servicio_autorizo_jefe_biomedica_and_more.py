# Generated by Django 4.2.3 on 2023-07-26 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0014_orden_servicio_num_mantenimiento_preventivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden_servicio',
            name='autorizo_jefe_biomedica',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orden_servicio',
            name='autorizo_jefe_conservacion',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orden_servicio',
            name='descripcion_servicio',
            field=models.CharField(max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='orden_servicio',
            name='estatus',
            field=models.CharField(choices=[('FUN', 'Equipo funcional'), ('OUT', 'Equipo fuera de servicio'), ('N/A', 'No se realizo servicio')], default='FUN', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='orden_servicio',
            name='fallo_paciente',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='orden_servicio',
            name='ing_realizo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='orden_servicio',
            name='responsable',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='orden_servicio',
            name='tipo_orden',
            field=models.CharField(choices=[('A', 'Orden agendada'), ('E', 'Orden espontanea'), ('B', 'Bitacora')], default='A', max_length=1),
        ),
    ]
