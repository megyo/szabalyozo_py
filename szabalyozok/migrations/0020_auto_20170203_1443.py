# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('szabalyozok', '0019_auto_20170130_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='szabalyozok',
            name='letesites_ev',
        ),
        migrations.AddField(
            model_name='muszerek',
            name='metrologia',
            field=models.CharField(choices=[('', 'Kérem válasszon'), ('H', 'Hitelesítendő'), ('K', 'Kalibrálandó'), ('FH', 'Helyszínen felülvizsgálandó'), ('FM', 'Műhelyben felülvizsgálandó'), ('T', 'Tájékoztató jellegű'), ('Cs', 'Cserélendő')], default='K', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='muszerek',
            name='telefon',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='diagnosztika',
            name='biztlef_nyomas',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='diagnosztika',
            name='p1_nyomas',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='diagnosztika',
            name='p2_nyomas',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='szabalyozok',
            name='grass_az',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
