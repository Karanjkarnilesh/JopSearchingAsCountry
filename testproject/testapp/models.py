# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Hyd_Job(models.Model):
    DATE=models.DateField()
    COMPANY=models.CharField(max_length=100)
    TITLE=models.CharField(max_length=100)
    ELIGIBILITY=models.CharField(max_length=100)
    ADDRESS=models.CharField(max_length=100)
    EMAIL=models.EmailField()
    PHONENUMBER=models.IntegerField()

class Mumbai_Job(models.Model):
    DATE=models.DateField()
    COMPANY=models.CharField(max_length=100)
    TITLE=models.CharField(max_length=100)
    ELIGIBILITY=models.CharField(max_length=100)
    ADDRESS=models.CharField(max_length=100)
    EMAIL=models.EmailField()
    PHONENUMBER=models.IntegerField()


class Pune_Job(models.Model):
    DATE=models.DateField()
    COMPANY=models.CharField(max_length=100)
    TITLE=models.CharField(max_length=100)
    ELIGIBILITY=models.CharField(max_length=100)
    ADDRESS=models.CharField(max_length=100)
    EMAIL=models.EmailField()
    PHONENUMBER=models.IntegerField()

class Bangalora_Job(models.Model):
    DATE=models.DateField()
    COMPANY=models.CharField(max_length=100)
    TITLE=models.CharField(max_length=100)
    ELIGIBILITY=models.CharField(max_length=100)
    ADDRESS=models.CharField(max_length=100)
    EMAIL=models.EmailField()
    PHONENUMBER=models.IntegerField()