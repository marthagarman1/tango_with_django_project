# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2019-02-04 15:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20190204_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2019, 2, 4, 15, 26, 56, 817138, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
