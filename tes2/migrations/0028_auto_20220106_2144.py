# Generated by Django 2.2 on 2022-01-07 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tes2', '0027_auto_20220106_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='hecatreas_trabajadas',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='transaccion',
            name='numero_hectareas',
            field=models.IntegerField(default=1),
        ),
    ]
