# Generated by Django 4.2.3 on 2023-08-02 00:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0021_reporteusuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporteusuario',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='area_reporte', to='inventario.area_hospital'),
        ),
        migrations.AlterField(
            model_name='reporteusuario',
            name='equipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipo_reporte', to='inventario.equipo_medico'),
        ),
        migrations.CreateModel(
            name='CheckList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bateria', models.CharField(choices=[('B', 'Buena'), ('M', 'Mala'), ('N', 'N/A')], max_length=1)),
                ('condicion_general', models.CharField(choices=[('B', 'Buena'), ('M', 'Mala'), ('N', 'N/A')], max_length=1)),
                ('enciende', models.BooleanField()),
                ('sensor_SPO2', models.CharField(choices=[('B', 'Buena'), ('M', 'Mala'), ('N', 'N/A')], default='N', max_length=1)),
                ('sensor_TEMP', models.CharField(choices=[('B', 'Buena'), ('M', 'Mala'), ('N', 'N/A')], default='N', max_length=1)),
                ('PANI', models.CharField(choices=[('B', 'Buena'), ('M', 'Mala'), ('N', 'N/A')], default='N', max_length=1)),
                ('sensor_ECG', models.CharField(choices=[('B', 'Buena'), ('M', 'Mala'), ('N', 'N/A')], default='N', max_length=1)),
                ('sensor_PAI', models.CharField(choices=[('B', 'Buena'), ('M', 'Mala'), ('N', 'N/A')], default='N', max_length=1)),
                ('observaciones', models.CharField(max_length=800)),
                ('desempeño_general', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='area_checklist', to='inventario.area_hospital')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipo_checklist', to='inventario.equipo_medico')),
            ],
        ),
    ]