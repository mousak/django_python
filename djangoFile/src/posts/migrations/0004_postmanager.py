# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-15 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20160115_0234'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
