# Generated by Django 2.2 on 2022-03-08 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tes2', '0006_auto_20220129_0600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud',
            name='aceptada_dueño',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='aceptada_solicitante',
        ),
        migrations.AddField(
            model_name='solicitud',
            name='quien_manda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sol_remitente', to='tes2.Usuario'),
        ),
    ]
