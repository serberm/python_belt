# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-15 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_trip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='plan',
            field=models.TextField(default='No plan yet...'),
        ),
    ]
