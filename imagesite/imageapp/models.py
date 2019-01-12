from django.db import models
#from PIL import Image
# Create your models here.
class ExampleModel(models.Model):
	name=models.CharField(max_length=30)
	model_pic = models.ImageField(upload_to = 'photo/%Y/%m/%d',blank=True,null=True)
	def __str_(self):
		return "id=%s,name=%s"%(self.id,self.name)
