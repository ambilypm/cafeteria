# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-05 06:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_delete_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('logo', models.ImageField(upload_to='logo')),
            ],
            options={
                'db_table': 'Item',
            },
        ),
    ]
