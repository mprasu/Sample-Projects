from django.shortcuts import render,render_to_response

# Create your views here.
from signup.forms import SignupForm
from signup.models import Usersinfo
from django import forms
def signupform(request):
	if request.method == 'POST':	#if form is submitted
		msg=""
		form = SignupForm(request.POST)
		if form.is_valid():
			fname=form.cleaned_data['firstname']
			lname=form.cleaned_data['lastname']
			email=form.cleaned_data['email']
			pwd=form.cleaned_data['password']
			confirmpwd=form.cleaned_data['confirmpassword']
			obj=Usersinfo(firstname=fname,lastname=lname,mailid=email,password=pwd)
			obj.save()
			return render(request, 'result.html', {'firstname': fname,'lastname':lname,'email': email,})
		else:
			return render(request, 'signup.html', {'form':form});	

	else:
		form = SignupForm()
		return render(request, 'signup.html', {'form':form});	#returning form 


# Create your views here.
def index(request):
    return render_to_response('index.html')
