# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-25 20:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0005_auto_20171025_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='userkey',
        ),
    ]
