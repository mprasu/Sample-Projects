from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse 
from django.views.generic import View
class Welcome(View):
	def get(self,request):
		return HttpResponse('<html><body><h1>\
hello welcome to class based views </h1>\
</body></html>')
class GetInput(View):
	def get(self,request):
		return render(request,"app6/classget.html")
class PostInput(View):
	def get(self,request):
		return render(request,"app6/classpost.html")

class Add(View):
	def get(self,request):
		try:
			a=int(request.GET['t1'])
			b=int(request.GET['t2'])
			c=a+b
			return HttpResponse("<html> <body bgcolor=red>\
<h1> sum is: "+ str(c) +"</h1> </body> </html>") 
		except(ValueError):
			return HttpResponse("invalid input")
	def post(self,request):
		try:
			a=int(request.POST['t1'])
			b=int(request.POST['t2'])
			c=a+b
			return HttpResponse("<html> <body bgcolor=red>\
<h1> sum is: "+ str(c) +"</h1> </body> </html>") 
		except(ValueError):
			return HttpResponse("invalid input")
