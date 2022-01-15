# Generated by Django 2.2 on 2022-01-15 03:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversacion',
            fields=[
                ('id_conversacion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('num_equipo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_equipo', models.CharField(default='', max_length=100)),
                ('tipo_equipo', models.CharField(choices=[('tractor', 'TRACTOR'), ('arado', 'ARADO'), ('rastra', 'RASTRA'), ('sembradora', 'SEMBRADORA'), ('pulverizadora', 'PULVERIZADORA'), ('cosechadora', 'COSECHADORA'), ('otros', 'OTROS')], max_length=20, null=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('marca', models.CharField(default='', max_length=20)),
                ('modelo', models.CharField(default='', max_length=20)),
                ('año', models.PositiveSmallIntegerField(default=1993)),
                ('estado_equipo', models.CharField(choices=[('malo', 'Malo'), ('regular', 'Regular'), ('buena', 'Buena'), ('excelente', 'Excelente')], max_length=10)),
                ('para_que', models.CharField(choices=[('venta', 'Venta'), ('renta', 'Renta'), ('ambos', 'Ambos')], max_length=10)),
                ('hecatreas_trabajadas', models.IntegerField(default=1)),
                ('precio_venta', models.FloatField(null=True)),
                ('precio_renta_dia', models.FloatField(null=True)),
                ('status', models.CharField(choices=[('activo', 'Activo'), ('apartado', 'Apartado'), ('rentado', 'Rentado'), ('inactivo', 'Inactivo'), ('eliminado', 'Eliminado')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Arado',
            fields=[
                ('id_equipo', models.OneToOneField(max_length=10, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tes2.Equipo')),
                ('tipo', models.CharField(max_length=20)),
                ('reversible', models.BooleanField(default=False)),
                ('no_cuerpos', models.PositiveSmallIntegerField()),
                ('neumatica_mecanica', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cosechadora',
            fields=[
                ('id_equipo', models.OneToOneField(max_length=10, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tes2.Equipo')),
                ('tipo_cultivo', models.CharField(max_length=20)),
                ('potencia', models.PositiveSmallIntegerField()),
                ('capacidad_granos', models.PositiveSmallIntegerField(null=True)),
                ('tasa_descarga', models.PositiveSmallIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Otros_equipos',
            fields=[
                ('id_equipo', models.OneToOneField(max_length=10, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tes2.Equipo')),
                ('potencia', models.PositiveSmallIntegerField(null=True)),
                ('producto_agricola', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pulverizadora',
            fields=[
                ('id_equipo', models.OneToOneField(max_length=10, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tes2.Equipo')),
                ('autopropulsada', models.BooleanField(default=False)),
                ('tamaño_tanque', models.PositiveSmallIntegerField()),
                ('no_boquillas', models.PositiveSmallIntegerField()),
                ('capacidad_bomba', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rastra',
            fields=[
                ('id_equipo', models.OneToOneField(max_length=10, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tes2.Equipo')),
                ('acople', models.CharField(max_length=20)),
                ('tipo_cuerpo', models.CharField(max_length=20)),
                ('no_cuerpos', models.PositiveSmallIntegerField()),
                ('disposicion_cuerpos', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Sembradora',
            fields=[
                ('id_equipo', models.OneToOneField(max_length=10, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tes2.Equipo')),
                ('tipo', models.CharField(max_length=20)),
                ('fertilizadora', models.BooleanField(default=False)),
                ('no_tolvas', models.PositiveSmallIntegerField()),
                ('neumatica_mecanica', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Tractor',
            fields=[
                ('id_equipo', models.OneToOneField(max_length=10, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tes2.Equipo')),
                ('potencia', models.CharField(max_length=4)),
                ('estrias_PTO', models.CharField(max_length=2)),
                ('enganche_tres_puntos', models.BooleanField()),
                ('traccion', models.CharField(max_length=9)),
                ('cabina', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=25, null=True)),
                ('apellido_1', models.CharField(max_length=30, null=True)),
                ('apellido_2', models.CharField(blank=True, max_length=30, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('celular', models.CharField(max_length=20)),
                ('nivel_permisos', models.PositiveSmallIntegerField(default=1)),
                ('usuario_activo', models.BooleanField(default=True)),
                ('id_usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id_ubicacion', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('alias', models.CharField(max_length=40)),
                ('coord_x', models.CharField(max_length=20)),
                ('coord_y', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=70, null=True)),
                ('municipio', models.CharField(max_length=100, null=True)),
                ('referencias', models.CharField(max_length=200)),
                ('area', models.PositiveSmallIntegerField(default=1)),
                ('eliminado', models.BooleanField(default=False)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tes2.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id_transaccion', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('estatus', models.CharField(choices=[('1', 'Completada'), ('2', 'Abortada'), ('3', 'En Ejecución'), ('4', 'En Espera')], max_length=12)),
                ('fecha_inicial', models.DateField(default='2021-06-22')),
                ('fecha_final', models.DateField(blank=True, null=True)),
                ('importe_total', models.FloatField()),
                ('numero_hectareas', models.IntegerField(default=1)),
                ('tipo_transaccion', models.CharField(max_length=5)),
                ('desde_donde', models.ForeignKey(default='0001', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='desde_donde_ubicacion', to='tes2.Ubicacion')),
                ('hacia_donde', models.ForeignKey(default='0002', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='hacia_donde_ubicacion', to='tes2.Ubicacion')),
                ('id_arrendatario', models.ForeignKey(default='0001', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='arrendatario_usuario', to='tes2.Usuario')),
                ('id_dueño', models.ForeignKey(default='0001', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='dueño_usuario', to='tes2.Usuario')),
                ('id_equipo', models.ForeignKey(default='0001', on_delete=django.db.models.deletion.SET_DEFAULT, to='tes2.Equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id_solicitud', models.AutoField(primary_key=True, serialize=False)),
                ('comentario', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_operacion', models.CharField(max_length=5)),
                ('fecha_solicitud', models.DateField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField(blank=True, null=True)),
                ('estatus', models.CharField(choices=[('1', 'En Espera'), ('2', 'Visto'), ('3', 'Aceptada'), ('4', 'Rechazada')], max_length=10)),
                ('costo', models.IntegerField()),
                ('tipo_solicitud', models.PositiveSmallIntegerField(default=1)),
                ('a_donde', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='hacia_donde_sol', to='tes2.Ubicacion')),
                ('desde_donde', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='dsde_donde_sol', to='tes2.Ubicacion')),
                ('id_dueño_eq', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sol_dueño', to='tes2.Usuario')),
                ('id_equipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tes2.Equipo')),
                ('id_solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sol_sol', to='tes2.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id_mensaje', models.AutoField(primary_key=True, serialize=False)),
                ('contenido', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('id_conversacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tes2.Conversacion')),
                ('remitente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id_imagen', models.AutoField(primary_key=True, serialize=False)),
                ('imagen', models.ImageField(blank=True, upload_to='images/')),
                ('es_principal', models.BooleanField(default=False)),
                ('id_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tes2.Equipo')),
            ],
        ),
        migrations.AddField(
            model_name='equipo',
            name='donde_esta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='donde_esta', to='tes2.Ubicacion'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='id_dueño',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='equipo',
            name='ubicacion_base',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ubcacion_base', to='tes2.Ubicacion'),
        ),
        migrations.AddField(
            model_name='conversacion',
            name='id_transaccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tes2.Transaccion'),
        ),
        migrations.AddField(
            model_name='conversacion',
            name='usuario_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usr_1_convo', to='tes2.Usuario'),
        ),
        migrations.AddField(
            model_name='conversacion',
            name='usuario_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usr_2_convo', to='tes2.Usuario'),
        ),
    ]
