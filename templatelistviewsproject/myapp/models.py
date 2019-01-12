from django.db import models

# Create your models here.
from django.db import models
class suprabat_rooms(models.Model):
	roomnumber = models.IntegerField(primary_key=True)
	roomtype = models.CharField(max_length=50)
	aminity = models.CharField(max_length=8)
	cost = models.DecimalField(max_digits=10,decimal_places=4)
	booked = models.CharField(max_length=5)