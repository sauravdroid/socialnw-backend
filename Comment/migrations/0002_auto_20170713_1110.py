# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 11:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commented_at',
            field=models.DateField(default=datetime.datetime(2017, 7, 13, 11, 10, 24, 654046, tzinfo=utc)),
        ),
    ]
