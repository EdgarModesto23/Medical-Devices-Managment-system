# Generated by Django 4.2.3 on 2023-07-16 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0010_alter_proveedor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]