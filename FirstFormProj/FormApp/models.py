	from django.db import models

# Create your models here.
class Employee(models.Model):
	eid=models.CharField(max_length=20,primary_key=True)
	ename=models.CharField(max_length=100)
	email=models.EmailField()
	class Meta:
		db_table="employee"