# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 19:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Comment', '0004_auto_20170717_1939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='comment',
        ),
        migrations.AlterField(
            model_name='comment',
            name='commented_at',
            field=models.DateField(default=datetime.datetime(2017, 7, 17, 19, 52, 33, 911996, tzinfo=utc)),
        ),
    ]