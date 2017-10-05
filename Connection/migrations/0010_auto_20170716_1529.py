# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 15:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Connection', '0009_auto_20170716_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='follower_since',
            field=models.DateField(default=datetime.datetime(2017, 7, 16, 15, 29, 42, 135751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='following',
            name='following_since',
            field=models.DateField(default=datetime.datetime(2017, 7, 16, 15, 29, 42, 136352, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='request',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2017, 7, 16, 15, 29, 42, 137061, tzinfo=utc)),
        ),
    ]
