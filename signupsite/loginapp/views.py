from django.shortcuts import render,render_to_response
from django.http import HttpResponse
# Create your views here.
from signup.forms import SignupForm
from loginapp.forms import LoginForm
from signup.models import Usersinfo
from django import forms
def LoginChk(request):
     if 'mail_id' not in request.session:
          if request.method == 'POST':
               form = LoginForm(request.POST)
               if form.is_valid():
                   mail=form.cleaned_data['email']
                   request.session['mail_id']=mail
                   request.session.set_expiry(300)
                   return render_to_response('inbox.html')
               else:
                   return render(request,'login.html',{'form':form})
          else:
               form = LoginForm()
               return render(request, 'login1.html', {'form':form});	#returning form 
     else:
          return render_to_response('inbox.html')
     

def logout(request):
	del request.session['mail_id']
	return HttpResponse("<strong>You are logged out.</strong>")


           #request.session['mail_id']=mail
                              #request.session.set_expiry(300)
                   #request.session.set_expiry(300)
		
