# Generated by Django 2.0.5 on 2018-06-11 04:26

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0003_calculadorapiramidal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculadorapiramidal',
            name='grupos_prociones',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='calculadorapiramidal',
            name='total_kcal',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='calculadorapiramidal',
            name='vct',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
