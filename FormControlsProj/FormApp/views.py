from django.shortcuts import render
from django.views.generic import View
from FormApp.models import HotelSuprabat
from FormApp.forms import TestForm
class TestView(View):
	
	def get(self,request):
		return render(request,'test.html',{"form":TestForm})	
	def post(self,request):
		form=TestForm(request.POST)
		if(form.is_valid()):
			roomid=form.cleaned_data['roomnumber']
			rec=HotelSuprabat.objects.filter(roomnumber=roomid)
			form.cleaned_data['roomtype']=rec[0].roomtype
			return render(request,"test.html",{"form":form})
		else:
			return render(request,'test.html',{"form":TestForm})