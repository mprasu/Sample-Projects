from django.db import models

# Create your models here.
class HotelSuprabat(models.Model):
	roomnumber = models.IntegerField(primary_key=True)
	roomtype = models.CharField(max_length=50)
	aminity = models.CharField(max_length=8)
	cost = models.DecimalField(max_digits=10,decimal_places=4)
	booked = models.CharField(max_length=5)
	def __str__(self):
		return "%s,%s,%s,%s,%s"%(str(self.roomnumber),self.roomtype,self.aminity,str(self.cost),self.booked)