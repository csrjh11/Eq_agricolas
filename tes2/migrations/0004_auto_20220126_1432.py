# Generated by Django 2.2 on 2022-01-26 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tes2', '0003_auto_20220126_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='desde_donde',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dsde_donde_sol', to='tes2.Ubicacion'),
        ),
    ]
