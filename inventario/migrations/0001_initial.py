# Generated by Django 4.2.4 on 2023-10-29 13:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Area_hospital",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre_sala", models.CharField(max_length=100)),
                (
                    "responsable",
                    models.ManyToManyField(
                        related_name="responsable_area", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "ordering": ["nombre_sala"],
            },
        ),
        migrations.CreateModel(
            name="Contrato",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("num_contrato", models.CharField(max_length=100, unique=True)),
                (
                    "tipo_contrato",
                    models.CharField(
                        choices=[
                            ("L", "Contrato local"),
                            ("G", "Contrato garantia"),
                            ("C", "Contrato consolidado"),
                        ],
                        default="L",
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "tipo_servicio_estipulado",
                    models.CharField(
                        choices=[
                            ("P/C", "Servicio preventivo y correctivo"),
                            ("PRV", "Servicio  preventivo"),
                            ("N/A", "Proveedor no brinda servicio"),
                        ],
                        default="PRV",
                        max_length=3,
                    ),
                ),
                ("fecha_vencimiento", models.DateField()),
                ("num_servicios", models.PositiveIntegerField(null=True)),
            ],
            options={
                "ordering": ["proveedor"],
            },
        ),
        migrations.CreateModel(
            name="Equipo_medico",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("numero_nacional_inv", models.CharField(max_length=100, unique=True)),
                ("nombre_equipo", models.CharField(max_length=100)),
                (
                    "estado",
                    models.CharField(
                        choices=[
                            ("FUNC", "Equipo funcional"),
                            ("OUT", "Equipo fuera de servicio"),
                            ("SERV", "Equipo en mantenimiento"),
                            ("BAJA", "Equipo en proceso de baja"),
                        ],
                        default="FUNC",
                        max_length=4,
                    ),
                ),
                ("observaciones", models.CharField(max_length=255, null=True)),
                ("numero_serie", models.CharField(max_length=255, null=True)),
                ("marca", models.CharField(max_length=50, null=True)),
                ("modelo", models.CharField(max_length=50, null=True)),
                ("cama", models.PositiveIntegerField(null=True)),
                (
                    "carta_obsolescencia_tercero",
                    models.FileField(null=True, upload_to="Anexos"),
                ),
                (
                    "dictamen_tecnico_propio",
                    models.FileField(null=True, upload_to="Anexos"),
                ),
                ("minuta_baja", models.FileField(null=True, upload_to="Anexos")),
                (
                    "area",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="equipos_area",
                        to="inventario.area_hospital",
                    ),
                ),
                (
                    "contrato",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="equipos_contrato",
                        to="inventario.contrato",
                    ),
                ),
            ],
            options={
                "ordering": ["nombre_equipo"],
            },
        ),
        migrations.CreateModel(
            name="Orden_Servicio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "numero_orden",
                    models.CharField(max_length=255, null=True, unique=True),
                ),
                ("fecha", models.DateField()),
                (
                    "motivo",
                    models.CharField(
                        choices=[
                            ("C", "Correctivo"),
                            ("P", "Preventivo"),
                            ("D", "Diagnostico"),
                            ("R", "Refaccion"),
                        ],
                        default="P",
                        max_length=1,
                    ),
                ),
                (
                    "tipo_orden",
                    models.CharField(
                        choices=[
                            ("A", "Orden agendada"),
                            ("E", "Orden espontanea"),
                            ("B", "Bitacora"),
                        ],
                        default="A",
                        max_length=1,
                    ),
                ),
                (
                    "estatus",
                    models.CharField(
                        choices=[
                            ("FUN", "Equipo funcional"),
                            ("OUT", "Equipo fuera de servicio"),
                            ("N/A", "No se realizo servicio"),
                            ("PEN", "Pendiente"),
                        ],
                        default="PEN",
                        max_length=3,
                    ),
                ),
                ("responsable", models.CharField(max_length=100, null=True)),
                ("autorizo_jefe_biomedica", models.BooleanField(default=False)),
                ("autorizo_jefe_conservacion", models.BooleanField(default=False)),
                ("descripcion_servicio", models.CharField(max_length=2000, null=True)),
                ("equipo_complementario", models.CharField(max_length=200, null=True)),
                ("ing_realizo", models.CharField(max_length=100, null=True)),
                (
                    "num_mantenimiento_preventivo",
                    models.PositiveSmallIntegerField(null=True),
                ),
                ("fallo_paciente", models.BooleanField(null=True)),
                (
                    "orden_escaneada",
                    models.FileField(null=True, upload_to="Ordenes_servicio"),
                ),
                (
                    "contrato",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="contrato_orden",
                        to="inventario.contrato",
                    ),
                ),
                (
                    "equipo_medico",
                    models.ManyToManyField(
                        related_name="equipo_orden", to="inventario.equipo_medico"
                    ),
                ),
            ],
            options={
                "ordering": ["-fecha"],
            },
        ),
        migrations.CreateModel(
            name="Proveedor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre_proveedor", models.CharField(max_length=100)),
                ("contacto", models.CharField(max_length=100, null=True)),
            ],
            options={
                "ordering": ["nombre_proveedor"],
            },
        ),
        migrations.CreateModel(
            name="ReporteUsuario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "estado",
                    models.CharField(
                        choices=[
                            ("PEN", "Pendiente"),
                            ("COM", "Atendido"),
                            ("CER", "Cerrado"),
                        ],
                        default="PEN",
                        max_length=3,
                    ),
                ),
                ("correo", models.EmailField(max_length=254, null=True)),
                ("fecha_hora", models.DateTimeField(auto_now_add=True)),
                (
                    "falla",
                    models.CharField(
                        choices=[
                            ("NO/ENC", "El equipo no enciende"),
                            ("ALARMA", "El equipo marca error o alguna alarma"),
                            (
                                "SENSOR",
                                "Un sensor esta fallando(Brazalette de PANI, sensor de SPO2, Sensores ECG, etc.)",
                            ),
                            (
                                "NO/TRB",
                                "El equipo no trabaja de forma que deberia(No funcionan perillas, botones, pantalla tactil, etc.)",
                            ),
                            ("PAPEL", "Hace falta papel"),
                        ],
                        max_length=6,
                    ),
                ),
                ("descripcion", models.CharField(max_length=500, null=True)),
                ("solucion_tecnico", models.CharField(max_length=500, null=True)),
                ("equipo_complementario", models.CharField(max_length=500, null=True)),
                ("fecha_entrega", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "area",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="area_reporte",
                        to="inventario.area_hospital",
                    ),
                ),
                (
                    "equipo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="equipo_reporte",
                        to="inventario.equipo_medico",
                    ),
                ),
                (
                    "orden",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="inventario.orden_servicio",
                    ),
                ),
                (
                    "responsable",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="responsable_reporte",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-fecha_hora"],
            },
        ),
        migrations.CreateModel(
            name="Evento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha", models.DateField()),
                (
                    "tipo_evento",
                    models.CharField(
                        choices=[
                            ("CONTR", "Vencimiento de contrato"),
                            ("SERVC", "Servicio preventivo agendado"),
                            ("CAPAC", "Curso de capacitacion agendada"),
                            ("CHECK", "Chequeo al equipo agendado"),
                        ],
                        max_length=5,
                    ),
                ),
                (
                    "contrato",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventario.contrato",
                    ),
                ),
                (
                    "equipo_medico",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Evento_equipo",
                        to="inventario.equipo_medico",
                    ),
                ),
            ],
            options={
                "ordering": ["fecha"],
            },
        ),
        migrations.AddField(
            model_name="contrato",
            name="proveedor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="proveedor_contrato",
                to="inventario.proveedor",
            ),
        ),
        migrations.CreateModel(
            name="CheckList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha_hora", models.DateTimeField(auto_now_add=True)),
                (
                    "bateria",
                    models.CharField(
                        choices=[("B", "Buena"), ("M", "Mala"), ("N", "N/A")],
                        max_length=1,
                    ),
                ),
                (
                    "condicion_general",
                    models.CharField(
                        choices=[("B", "Buena"), ("M", "Mala"), ("N", "N/A")],
                        max_length=1,
                    ),
                ),
                ("enciende", models.BooleanField()),
                (
                    "prueba_funcionamiento",
                    models.CharField(
                        choices=[
                            (
                                "P",
                                "El equipo paso la prueba de funcionamiento correctamente",
                            ),
                            ("N", "El equipo no paso prueba de funcionamiento"),
                        ],
                        max_length=1,
                    ),
                ),
                (
                    "sensor_SPO2",
                    models.CharField(
                        choices=[("B", "Buena"), ("M", "Mala"), ("N", "N/A")],
                        default="N",
                        max_length=1,
                    ),
                ),
                (
                    "sensor_TEMP",
                    models.CharField(
                        choices=[("B", "Buena"), ("M", "Mala"), ("N", "N/A")],
                        default="N",
                        max_length=1,
                    ),
                ),
                (
                    "PANI",
                    models.CharField(
                        choices=[("B", "Buena"), ("M", "Mala"), ("N", "N/A")],
                        default="N",
                        max_length=1,
                    ),
                ),
                (
                    "sensor_ECG",
                    models.CharField(
                        choices=[("B", "Buena"), ("M", "Mala"), ("N", "N/A")],
                        default="N",
                        max_length=1,
                    ),
                ),
                (
                    "sensor_PAI",
                    models.CharField(
                        choices=[("B", "Buena"), ("M", "Mala"), ("N", "N/A")],
                        default="N",
                        max_length=1,
                    ),
                ),
                ("observaciones", models.CharField(max_length=800, null=True)),
                (
                    "desempeño_general",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")],
                        validators=[django.core.validators.MaxValueValidator(5)],
                    ),
                ),
                (
                    "area",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="area_checklist",
                        to="inventario.area_hospital",
                    ),
                ),
                (
                    "equipo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="equipo_checklist",
                        to="inventario.equipo_medico",
                    ),
                ),
            ],
            options={
                "ordering": ["-fecha_hora"],
            },
        ),
    ]
