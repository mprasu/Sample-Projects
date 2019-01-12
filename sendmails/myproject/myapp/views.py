# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response

# Create your views here.
from django.core.mail import send_mail,send_mass_mail,mail_admins,mail_managers
from django.http import HttpResponse
import datetime
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from myapp.forms import LoginForm
from django.views.decorators.csrf import requires_csrf_token
from myapp.models import UserInfo,Inbox
from myapp.forms import SendMailForm,ComposeForm
#def welcome(request):
#   return render(request,"hello.html", {})


#def viewArticle(request, month, year):
#   text = "Displaying articles of : %s/%s"%(year, month)
#   return HttpResponse(text)


def viewArticle(request, articleId):
   """ A view that display an article based on his ID"""
   text = "Displaying article Number : %s" %articleId
   return redirect(viewArticles, month = '11', year = '2045')


def viewArticles(request, month, year):
   text = "Displaying articles of : %s/%s" % (year, month)
   return HttpResponse(text)


def welcome(request):
   today = datetime.datetime.now().date()
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return redirect("https://www.djangoproject.com")

def sendSimpleEmail(request):
	if request.method=='POST':
		form=SendMailForm(request.POST)
		if form.is_valid():
			subject=form.cleaned_data['subject']
			msg=form.cleaned_data['message']
			mail=form.cleaned_data['mailid']
			res = send_mail(subject,msg, "satya.gagan.n@gmail.com", [mail])
			return render_to_response("message.html")
	else:
		form=SendMailForm()
		return render(request,"mailbox.html",{'form':form})

	
def sendEmailWithAttach(request):
	if request.method=="POST":
		form=ComposeForm(request.POST)
		if form.is_valid():
			subj=form.cleaned_data['subject']
			bd=form.cleaned_data['body']	
			to=form.cleaned_data['to']
			attfile=form.cleaned_data['attachment']
			email = EmailMessage(subj,bd, "satya.gagan.n@gmail.com",[to])
			fd = open(attfile, 'r')
			email.attach(attfile, fd.read(), 'text/plain')
			email.send()
			return render_to_response("message.html")
	else:
		form=ComposeForm()
		return render(request,'mailbox.html',{'form':form})
		

def sendMassEmail(request):
 msg1 = ('hello', 'how are you', 'satya.gagan.n@gmail.com', ['nsatya.mcs@gmail.com'])
 msg2 = ('hai mohan', 'when will you come back', 'satya.gagan.n@gmail.com', ['krishna.mca959@gmail.com'])
 res = send_mass_mail((msg1, msg2), fail_silently = False)
 return HttpResponse('%s'%res)

def sendAdminsEmail(request):
	res = mail_admins('my subject', 'site is going down.')
	return HttpResponse('%s'%res)

def sendManagersEmail(request):
   res = mail_managers('my subject 2', 'Change date on the site.')
   return HttpResponse('%s'%res)



def login(request):
   if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)
      if MyLoginForm.is_valid():
           uname = MyLoginForm.cleaned_data['username']
           pwd = MyLoginForm.cleaned_data['password']
           user=UserInfo.objects.filter(username=uname,password=pwd)
           if(user):
             mails=Inbox.objects.filter(username_id=list(user)[0].id)
             return render(request,'loggedin.html',{'username':uname,'emails':mails})
           else:
             return render(request,'login.html',{"form":MyLoginForm,"message":"invalid username/password"})
   else:
      MyLoginForm = LoginForm()
      return render(request,'login.html',{"form":MyLoginForm,"message":""})          
   

