# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('szabalyozok', '0011_doc'),
    ]

    operations = [
        migrations.AddField(
            model_name='muszerkiszerel',
            name='selejt',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
