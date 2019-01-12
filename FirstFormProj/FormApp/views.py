from django.shortcuts import render
from .forms import EmployeeForm
from django.http import HttpResponse
from .models import Employee
# Create your views here.
def emp(request):
	if request.method=="POST":
		form=EmployeeForm(request.POST)
		if form.is_valid():
			form.save();
			return render(request,"link.html",{"msg":"data submitted succ.."})
		else:
			form=EmployeeForm()
			return render(request,"index.html",{"form":form})
	else:
		form=EmployeeForm()
		return render(request,"index.html",{"form":form})
def display(request):
	recs=Employee.objects.all()
	return render(request,"display.html",{'records':recs})