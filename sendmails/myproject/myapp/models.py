# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models

class UserInfo(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=50)
	
class Inbox(models.Model):
	username=models.ForeignKey(UserInfo,on_delete=models.CASCADE)
	subject=models.CharField(max_length=30)
	message=models.CharField(max_length=50)

