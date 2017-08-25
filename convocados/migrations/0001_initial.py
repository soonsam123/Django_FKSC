# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-25 12:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Convocado_campeonato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_campeonato', models.CharField(max_length=400)),
                ('est_cidade', models.CharField(max_length=100)),
                ('data', models.CharField(max_length=50)),
                ('cartaz', models.FileField(default='/static/images/logo.jpg', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Convocados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=500)),
                ('academia', models.CharField(max_length=200)),
                ('faixa', models.CharField(max_length=100)),
                ('reg_fed', models.IntegerField()),
                ('Convocado_campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='convocados.Convocado_campeonato')),
            ],
        ),
    ]