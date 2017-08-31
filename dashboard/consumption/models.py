# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserData(models.Model):
    user_id = models.IntegerField()
    area = models.CharField(max_length=50)
    tariff = models.CharField(max_length=50)

class Consumption(models.Model):
    user = models.ForeignKey(UserData, on_delete=models.CASCADE)
    datetime = models.DateTimeField(null=True)
    consumption = models.FloatField()

class Aggregation(models.Model):
    date = models.DateField(null=True)
    total = models.FloatField()
    average = models.FloatField()    

