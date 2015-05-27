# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='imagen_destacada',
            field=models.ImageField(default='default.jpg', upload_to='main_pics/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articulo',
            name='estado',
            field=models.CharField(default='p', choices=[('b', 'borrador'), ('p', 'publicado')], max_length=1),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='slug',
            field=models.SlugField(blank=True, null=True, editable=False),
        ),
    ]
