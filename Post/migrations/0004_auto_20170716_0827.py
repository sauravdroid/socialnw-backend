# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 08:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0003_auto_20170714_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2017, 7, 16, 8, 27, 11, 927345, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='subheader',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='postlike',
            name='liked_at',
            field=models.DateField(default=datetime.datetime(2017, 7, 16, 8, 27, 11, 927960, tzinfo=utc)),
        ),
    ]