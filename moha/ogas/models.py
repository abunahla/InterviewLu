# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Reg(models.Model):
	firstname = models.CharField(max_length=20)
	secondname = models.CharField(max_length=20)
	companyname = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	logo = models.CharField(max_length=500)
