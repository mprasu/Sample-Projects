
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
	image = models.ImageField(upload_to='profile_image', blank=True)
	
	def __str__(self):
		return self.Name

class Events(models.Model):
	Name=models.CharField(max_length=50)
	Yourevent=models.TextField(max_length=200)
	Date=models.DateField()
	Time=models.TimeField()


	def __str__(self):
		return self.Name
class signupchild(models.Model):
	Name=models.CharField(max_length=25)
	Phonenumber=models.IntegerField()
	msg=models.CharField(max_length=250)




	def __str__(self):
		return self.Name
class gallery(models.Model):
	images=models.ImageField(upload_to='media',default='')

# Create your models here.
