# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0019_auto_20170106_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='question',
        ),
        migrations.AddField(
            model_name='status',
            name='question',
            field=models.ManyToManyField(blank=True, null=True, to='quiz.Question'),
        ),
    ]