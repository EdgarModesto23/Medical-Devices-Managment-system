# Generated by Django 4.2.4 on 2023-08-22 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0032_alter_orden_servicio_orden_escaneada'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden_servicio',
            name='proveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proveedor_orden', to='inventario.proveedor'),
        ),
    ]
