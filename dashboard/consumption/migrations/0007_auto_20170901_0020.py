# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-01 00:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consumption', '0006_auto_20170831_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumption',
            name='user',
        ),
        migrations.DeleteModel(
            name='Consumption',
        ),
    ]
