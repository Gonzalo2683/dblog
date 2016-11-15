# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 18:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=160)),
                ('descripcion', models.TextField()),
                ('orden', models.IntegerField(default=0)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.Curso')),
            ],
        ),
    ]
