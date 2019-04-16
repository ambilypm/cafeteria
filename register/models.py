# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=100)
    phonenumber=models.IntegerField()
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    class Meta:
        db_table='reg'

class Items(models.Model):
    quantity = models.IntegerField()
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    logo=models.ImageField(upload_to='logo')

    class Meta:
        db_table='Item'

class Order(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    logo=models.CharField(max_length=100)
    date=models.CharField(max_length=300)
    quantity=models.IntegerField()

    class Meta:
        db_table='Order'