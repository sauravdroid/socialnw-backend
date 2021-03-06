# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 19:13
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Connection', '0012_auto_20170716_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='follower_since',
            field=models.DateField(default=datetime.datetime(2017, 7, 16, 19, 13, 39, 727075, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='following',
            name='following_since',
            field=models.DateField(default=datetime.datetime(2017, 7, 16, 19, 13, 39, 727712, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='request',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2017, 7, 16, 19, 13, 39, 728437, tzinfo=utc)),
        ),
        migrations.AlterUniqueTogether(
            name='request',
            unique_together=set([('user', 'requested_user')]),
        ),
    ]
