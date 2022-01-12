# Generated by Django 2.2 on 2021-12-06 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tes2', '0014_conversacion_mensaje'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificacion',
            name='id_transaccion',
        ),
        migrations.AddField(
            model_name='notificacion',
            name='id_solicitud',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='tes2.Solicitud'),
            preserve_default=False,
        ),
    ]
