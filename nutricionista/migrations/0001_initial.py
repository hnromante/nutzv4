# Generated by Django 2.0.5 on 2018-05-31 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('superadmin', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('alimentos', models.ManyToManyField(related_name='menus', to='superadmin.Alimento')),
            ],
        ),
        migrations.CreateModel(
            name='Nutricionista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_nutri', models.CharField(max_length=254)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nutricionista', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PautaAlimentaria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('recomendacion', models.CharField(default='Comer sanito', max_length=2000)),
                ('menus', models.ManyToManyField(to='nutricionista.Menu')),
                ('nutricionista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pautas_alimentarias', to='nutricionista.Nutricionista')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='nutricionista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutricionista.Nutricionista'),
        ),
    ]