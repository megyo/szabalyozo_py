# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('szabalyozok', '0017_auto_20170127_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosztika',
            name='p1_felso_nyomas',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='diagnosztika',
            name='p2_also_nyomas',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
    ]
