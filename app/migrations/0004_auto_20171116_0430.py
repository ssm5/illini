# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 04:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20171113_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='parents',
            field=models.ManyToManyField(blank=True, to='app.Tag'),
        ),
    ]
