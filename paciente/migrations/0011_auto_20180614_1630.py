# Generated by Django 2.0.5 on 2018-06-14 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0010_auto_20180614_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichageneral',
            name='ultima_atencion',
            field=models.DateField(blank=True, null=True),
        ),
    ]
