
from django.db import models

# Create your models here.
class signup(models.Model):
	Name=models.CharField(max_length=50)
	Age=models.IntegerField()
	Email_id=models.EmailField(max_length=80)
	Password=models.CharField(max_length=20)
	ConfirmPassword=models.CharField(max_length=20)
	Phonenumber=models.IntegerField()
	Location=models.CharField(max_length=50)
	State=models.CharField(max_length=50)
	Country=models.CharField(max_length=50)
	Address=models.CharField(max_length=50)
	file = models.ImageField(null=True,blank=True)



	def __str__(self):
		return self.Name



# Create your models here.
