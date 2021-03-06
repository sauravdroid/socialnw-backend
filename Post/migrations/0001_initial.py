# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 08:59
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('cover_pic', models.FileField(upload_to=b'')),
                ('subheader', models.CharField(max_length=60)),
                ('content', models.TextField()),
                ('created_at', models.DateField(default=datetime.datetime(2017, 7, 13, 8, 59, 0, 955137, tzinfo=utc))),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
