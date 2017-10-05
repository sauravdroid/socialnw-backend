# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 21:56
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_auto_20170713_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2017, 7, 14, 21, 56, 5, 384646, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='postlike',
            name='liked_at',
            field=models.DateField(default=datetime.datetime(2017, 7, 14, 21, 56, 5, 385310, tzinfo=utc)),
        ),
    ]
