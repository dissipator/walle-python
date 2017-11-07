# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
 
class Test(models.Model):
    name = models.CharField(max_length=20)

class Contact(models.Model):
	"""docstring for Concat"""
	name  = models.CharField(max_length=200)
	age   = models.IntegerField(default=0)
	email = models.EmailField()
	def __unicode__(self):
		return self.name

class Tag(models.Model):
	"""docstring for Tag"""
	contact = models.ForeignKey(Contact)
	name   = models.CharField(max_length=50)
	def __uncode__(self):
		return self.name
'''
```
|Tag  |        |Contact|
|+id  |---	   | +id   |
|+name|	 |-->  |+name  |
			   |+age   |
			   |+email |
'''