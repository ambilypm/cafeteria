# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-05 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='phonenumber',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
