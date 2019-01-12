
from django.shortcuts import render
from .models import signup, Events, signupchild
from django.http import *
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Q
from twilio.rest import Client


def signup1(request):
	if request.method == 'POST' and request.FILES['myfile']:
		b1 =request.POST['a1']# a1 is the name given for fileds in signup.html page
		b2 =request.POST.get('a2')
		b3=request.POST.get('a3')
		b4 =request.POST.get('a4')
		b5=request.POST.get('a5')
		b6=request.POST.get('a6')
		b7=request.POST.get('a7')
		b8=request.POST.get('a8')
		b9=request.POST.get('a9')
		b10=request.POST.get('a10')
		b11=request.FILES['myfile']
		myobj=signup.objects.all()#signup is my model name
		emailexist="This mail is already registered"
		e=0

		for j in myobj:
		 	if j.Email_id==b3:
		 		e=e+1
		if e>=1:
			return render(request,'signup.html',{'emailexist':emailexist})
		else:	
		 	f=signup(Name=b1,Age=b2,Email_id=b3,Password=b4,ConfirmPassword=b5,Phonenumber=b6,Location=b7,State=b8,Country=b9,Address=b10,document=b11,)
		 	f.save()
		 	success_message="Your registration is success Now you can login"
		 	return render(request,'home.html',{"success_message_key":success_message})

	return render(request,'signup.html')	


def home(request):
	return render(request,'home.html')


def login(request):
	if request.method == 'POST':
		name =request.POST.get('myname')
		password=request.POST.get('mypassword')
		obj=signup.objects.all()
		print("the object is",obj)
		msg1=" password dint matched"
		msg2="username dint matched"
		x=0
		for i in obj:
			if i.Name==name:
				x=x+1
				if i.Password==password:
					x=x+1
					uname=i.Name
		if x==2:
				return render(request,'afterlogin.html',{'uname':uname})
		if x==1:
				return render(request,'login.html',{'msg1':msg1})
		else:
				return render(request,'login.html',{'msg2':msg2})		

	else:
		
		return render(request,'login.html')	


def forgetpassword(request):
	if request.method == 'POST':

		email =request.POST.get('email')
		number=request.POST.get('number')
		mydbobj=signup.objects.all()
		phone_missmatch=" phone number dint matched"
		Email_missmatch="email dint matched"
		passwordsent="Your password has been sent to your mail"
	
		y=0
		for j in mydbobj:
			if j.Email_id==email:
				subject = "Your password"
				contact_massage = j.Password
				From_email = 'pd.poojachary95@gmail.com'
				To_email = [email]
				send_mail(subject, contact_massage, From_email, To_email, fail_silently=False)
				return render(request,'login.html',{'passwordsent':passwordsent})
		else:
			return render(request,'forgetpassword.html',{'Email_missmatch':Email_missmatch})
	return render(request,'forgetpassword.html')

def location(request):#search based on location and name
	if request.method=='POST':
			name2=request.POST.get('name')
			location2=request.POST.get('loc')
			print("result",name2)
			match=signup.objects.filter(Location__contains=location2,Name__contains=name2)
			msg="no result found"
			if match:
				return render(request,'location.html',{'sr':match})
			else:
				return render(request,'location.html',{'msg':msg})
	return render(request,'location.html')

def viewdetails(request):#hyperlink to view more details about person
	query=request.GET['query']
	x=query.split(',')
	print(x[0],x[1])
	mydb=signup.objects.filter(Location__exact=x[0],Name__exact=x[1])
	return render(request,'viewdetails.html',{'mydb':mydb})

def mySettings(request):
	return render(request,"settings.html")

def changepassword(request):
	if request.method=='POST':
		email=request.POST.get('a1')
		oldPassword=request.POST.get('a2')
		password=request.POST.get('a3')
		confirmPassword=request.POST.get('a4')
		mydata=signup.objects.all()
		x=0
		for i in mydata:
			if i.Email_id==email:
				x=x+1
				if i.Password==oldPassword:
					x=x+1
		if x==0:
			return render(request,"changepassword.html",{'mailDoesnotExist':"mailDoesnotExist"})
		if x==1:
			return render(request,"changepassword.html",{'wrongPassword':"Enter valid password"})
		else:
			i.Password=password
			i.ConfirmPassword=confirmPassword
			i.save()
			return render(request,"changepassword.html",{'success':"Successfully your password is changed"})
	return render(request,"changepassword.html",)


def deleteAccount(request):
	if request.method=='POST':
		Email=request.POST.get('email')
		pasword=request.POST.get('mypassword')
		mydbs=signup.objects.all()
		x=0
		for i in mydbs:
			print(i.Email_id)
			if i.Email_id==Email and i.Password==pasword:
				x=x+1
		if x==1:
			i.delete()
			return render(request,'deleteAccount.html',{'success':"success"})
		else:
			return render(request,'deleteAccount.html',{'mailDoesnotExist':"mailDoesnotExist"})

	return render(request,'deleteAccount.html')


def contact(request):#hyperlink 
	l=[]
	for ascii in range(65,90):
		l.append(chr(ascii))
	return render(request,'contact.html',{'letters':l})


def filter_data(request):#searching  alphabetical wise 
	query=request.GET['query']
	f=signup.objects.filter(Name__startswith=query)
	return render(request,'filter_data.html',{'f':f})

def editprofile(request):

	query=request.GET['query']
	fltr=signup.objects.filter(Name__exact=query)
	
	if request.method=='POST':
		name=request.POST.get('a1')
		age=request.POST.get('a2')
		email=request.POST.get('a3')
		phonenumber=request.POST.get('a6')
		location=request.POST.get('a7')
		state=request.POST.get('a8')
		country=request.POST.get('a9')
		address=request.POST.get('a10')
		document=request.POST.get('myfile')
		mydb=signup.objects.all()
		z=0
		for j in mydb:
			if j.Email_id==email:
				z=z+1
		if z==1:
			j.Name=name
			j.Age=age
			j.Phonenumber=phonenumber
			j.Location=location
			j.state=state
			j.country=country
			j.Address=address
			j.document=document
			j.save()
			return render(request,'afterlogin.html',{'success':"success"})
	return render(request,'editprofile.html',{'fltr':fltr})
	

def myevents(request):
	if request.method=='POST':
		name=request.POST.get('a1')#a1 is name in html fields
		events=request.POST.get('a2')
		date=request.POST.get('a3')
		time=request.POST.get('a4')
		mydb=Events.objects.all()
		print(date)
		print(time)
		x=0
		for i in mydb:
			j=str(i.Date)
			f=j.split('-')#-->spliting model date
			ij=str(date)
			ik=ij.split('-')#-->spliting html date
			m=str(i.Time)
			mm=m.split(':')
			n=str(time)
			nn=n.split(':')

			if f[0]==ik[0] and f[1]==ik[1] and f[2]==ik[2]:
				if mm[0]==nn[0]:
					print(f[0],ik[0])
					x=x+1
		if x==1:
			msg="This shift is alredy booked please choose another shift"
			return render(request,'myevents.html',{'msg':msg})
		else:
			f=Events(Name=name,Yourevent=events,Date=date,Time=time)#Events is model name
			f.save()
			return render(request,'myevents.html')
	return render(request,'myevents.html')

def sendingSMS(request):
	if "yournumber" in request.POST and "yourpassword" in request.POST and "phonenumber" in request.POST and "message" in request.POST:
		ynumber=request.POST['yournumber']
		ypassword=request.POST['yourpassword']
		pnumber=request.POST['phonenumber']
		msge=request.POST.get['message']
		zerosms.sms(phno=ynumber,passwd=yourpassword,receivernum=phonenumber,message=msge)
		return HttpResponse("send")
	return HttpResponse(render(request,"sendingSMS.html", {}))
def media(request):
 	return render(request,"media.html")
def twiliosms(request):
	account_id='xx'
	auth_token='xx'
	client=Client(account_id,auth_token)
	message=client.messages.create(from_='+xx',body="Hai we have new offers this month CMR Shopping",to='+919014177369')
	return render(request,"twiliosms.html")



from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from email.mime.image import MIMEImage


def massmail(request):
    l=[]
    mails=signup.objects.all()
    for mail in mails:
        l.append(mail.Email_id)
    img_data = open("index.png", 'rb').read()
    img = MIMEImage(img_data)

    subject, from_email, recipient_list = 'Delveip-news letter', 'settings.EMAIL_HOST_USER', l
    text_content = 'This is an important message.'
    html_content = '<h1><p>Thank you<strong>for</strong>subscribing...</p></h1>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.attach(img)
    msg.send()
    return render(request,"massmail.html")

# Create your views here.







