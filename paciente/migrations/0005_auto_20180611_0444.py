# Generated by Django 2.0.5 on 2018-06-11 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0004_auto_20180611_0426'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calculadorapiramidal',
            old_name='grupos_prociones',
            new_name='grupos_porciones',
        ),
    ]
