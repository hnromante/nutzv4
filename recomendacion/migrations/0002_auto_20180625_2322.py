# Generated by Django 2.0.5 on 2018-06-25 23:22

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recomendacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recomendacion',
            name='comidas',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
