# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 17:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0023_auto_20170106_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='question',
        ),
        migrations.RemoveField(
            model_name='status',
            name='user',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]