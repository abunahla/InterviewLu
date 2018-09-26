# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class profile(models.Model):
	name = models.CharField(max_length=20)
	description = models.TextField(default="Enter Desription Here")
	location = models.CharField(max_length=50, default="Enter Is Your location")
	def __unicode__(self):
		return self.name

 