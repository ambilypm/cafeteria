# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Admin(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    class Meta:
         db_table='admin'