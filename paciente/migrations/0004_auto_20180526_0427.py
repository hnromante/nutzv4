# Generated by Django 2.0.5 on 2018-05-26 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0003_auto_20180526_0347'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='c_braquial',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='cintura',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='h_g_t',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='imc',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='p_bicipital',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='p_sub_escapular',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='p_sub_iliaco',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='p_tripicital',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='presion_arterial',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='talla',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='peso',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]