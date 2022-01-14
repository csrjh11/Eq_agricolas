# Generated by Django 2.2 on 2022-01-14 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tes2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='costo',
            field=models.IntegerField(default=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='id_dueño_eq',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sol_dueño', to='tes2.Usuario'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='id_equipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tes2.Equipo'),
        ),
    ]
