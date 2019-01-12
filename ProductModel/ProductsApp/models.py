# Create your models here.
from django.db import models
class Product(models.Model):
	pid = models.IntegerField(primary_key=True)# it is used to store only integer
	pname = models.CharField(max_length=20)#it is used to a small to medium sized string
	pcost = models.DecimalField (max_digits=10,decimal_places=4)
	pmfd = models.DateField()# to store date,lly to python datetime.date
	pexpd= models.DateField()