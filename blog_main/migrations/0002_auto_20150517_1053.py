# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='slug',
            field=models.SlugField(blank=True, null=True, editable=False),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='slug',
            field=models.SlugField(blank=True, null=True, editable=False),
        ),
    ]
