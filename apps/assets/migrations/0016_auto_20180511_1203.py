# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-11 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0015_auto_20180510_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='value',
            field=models.CharField(max_length=128, verbose_name='Value'),
        ),
    ]