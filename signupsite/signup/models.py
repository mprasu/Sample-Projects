from django.db import models

# Create your models here.

from django.db import models
class Usersinfo(models.Model):
	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	mailid = models.EmailField()
	password = models.CharField(max_length=30)


	
