# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-02 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0007_auto_20170501_0308'),
    ]

    operations = [
        migrations.AddField(
            model_name='frame',
            name='h',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='frame',
            name='w',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='region',
            name='polygon_points_json',
            field=models.TextField(default='[]'),
        ),
    ]
