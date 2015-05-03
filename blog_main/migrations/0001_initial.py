# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('modificado_en', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('modificado_en', models.DateTimeField(auto_now=True)),
                ('titulo', models.CharField(max_length=50, unique=True)),
                ('contenido', models.TextField()),
                ('slug', models.SlugField()),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ForeignKey(to='blog_main.Categoria')),
            ],
            options={
                'verbose_name': 'Entrada',
                'verbose_name_plural': 'Entradas',
            },
        ),
    ]
