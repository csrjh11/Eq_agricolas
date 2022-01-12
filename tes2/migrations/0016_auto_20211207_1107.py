# Generated by Django 2.2 on 2021-12-07 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tes2', '0015_auto_20211206_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud',
            name='completada',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='param_1',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='param_2',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='param_3',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='param_4',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='tipo_equipo',
        ),
        migrations.AddField(
            model_name='solicitud',
            name='estatus',
            field=models.CharField(choices=[('1', 'En Espera'), ('2', 'Visto'), ('3', 'Aceptada'), ('4', 'Rechazada')], default='1', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud',
            name='id_equipo',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='tes2.Equipo'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Notificacion',
        ),
    ]