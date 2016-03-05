# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-15 02:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2016, 1, 15, 2, 34, 18, 287532, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
