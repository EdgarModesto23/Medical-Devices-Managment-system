# Generated by Django 4.2.3 on 2023-07-31 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_cargo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cargo',
            field=models.CharField(choices=[('Ingeniero', 'Ingeniero'), ('Jefe', 'Jefe'), ('Admin', 'Administrador')], max_length=9),
        ),
    ]