
from django.shortcuts import render
from .models import signup
from django.http import *
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from email.mime.image import MIMEImage


# Create your views here.

def home(request):
	return render(request,"home.html")
# def signup2(request):
#     return render(request,'signup.html')
    
def signup1(request):
	if request.method == 'POST' and request.FILES['f1']:
		b1 =request.POST.get('a1')
		b2 =request.POST.get('a2')
		b3=request.POST.get('a3')
		b4 =request.POST.get('a4')
		b5=request.POST.get('a5')
		b6=request.POST.get('a6')
		b7=request.POST.get('a7')
		b8=request.POST.get('a8')
		b9=request.POST.get('a9')
		b10=request.POST.get('a10')
		DEmail=signup.objects.all()
		uploadimage=request.FILES['f1']
		msg3="This Name already exist please goto  login"
		z=0
		for i in DEmail:
			if i.Name==b1:
				z=z+1
		if(z>=1):
			return render(request,'signup.html',{'msg3':msg3})
		else:
			f=signup(Name=b1,Age=b2,Email_id=b3,Password=b4,ConfirmPassword=b5,Phonenumber=b6,Location=b7,State=b8,Country=b9,Address=b10,file=uploadimage)
			f.save()
			return render(request,'signup.html')
	return render(request,'signup.html')	


# def home(request):
# 	return render(request,'home.html')
def login(request):
	if request.method == 'POST':
		name =request.POST.get('h1')
		password=request.POST.get('h4')
		obj=signup.objects.all()
		msg1="Please check your Password"
		msg2="Please check your Username"
		y=0
		for i in obj:
			print(i)
			if i.Name==name:
				uname=i.Name
				y=y+1
				if i.Password==password:
					y=y+1

		if(y==2):
			return render(request,'afterlogin.html',{"paswd":uname})
		if (y==1):
			return render(request, 'login.html', {'msg1': msg1})
		else:
			return render(request,'login.html',{'msg2':msg2})
	else:
		return render(request,'login.html')
def resetpassword(request):
	dbusername=request.GET['query1']
	if request.method=='POST':
		cpassword=request.POST.get('cpswd')
		npassword=request.POST.get('npswd')
		cnpassword=request.POST.get('cnpswd')
		objs=signup.objects.all()

		for i in objs:
			if((i.Name==dbusername)and(i.Password==cpassword)):
				i.Password=npassword
				i.save()
				return render(request,'changepswd.html',{"msg5":"your password updated succussfully"})
		return render(request,'changepswd.html',{"msg6":"current password is wrong"})	
	return render(request,'changepswd.html')			
def password1(request):
	if request.method=='POST':
		username=request.POST.get('username')
		print(username)
		obj1=signup.objects.all()
		for user in obj1:
			if user.Name==username:
				passwor=user.Password
				subject = "Password reset Link"
				contact_message = "here ur password %s"%(passwor)
				From_email = settings.EMAIL_HOST_USER
				To_email = [user.Email_id]
				send_mail(subject, contact_message, From_email, To_email)

	return render(request,'password.html')

def searching(request):
	if request.method=='POST':
		location=request.POST.get('cntry')
		name1=request.POST.get('searc')
		print("name input",name1)
		res=signup.objects.filter(Location__contains=location,Name__contains=name1)
		msg="no result found"
		
		if res:
			return render(request,'search.html',{"match":res})
			
		else:
			return render(request, 'search.html',{'msg':msg})
	return render(request,'search.html',{})
def details(request):
    qset=request.GET['query']
    query=qset.split(',')
    match=signup.objects.filter(Location__exact=query[0],Name__exact=query[1])
    if qset:
        return render(request,'details.html',{'qset':match})
    else:
        return render(request,'details.html',{'msg':"value does not exist"})
def contacts(request):
	l=[]
	for ascii in range(65,90):
		l.append(chr(ascii))
	return render(request,'contacts.html',{'range':l})
def filter_data(request):

	letter=request.GET['query_nn']
	res=signup.objects.filter(Name__startswith=letter)
	return render(request,'filter.html',{'chr':res})
def updateprofile(request):
    q1=request.GET['query2']
    q2=signup.objects.filter(Name__exact=q1)
    z=0
    if request.method=='POST':
        for i in q2:
            if i.Name==q1:
                i.Age=request.POST.get('age')
                i.Address=request.POST.get('address')
                i.Country=request.POST.get('courntry')
                i.Email_id=request.POST.get('email')
                i.Location=request.POST.get('location')
                i.Phonenumber=request.POST.get('phonenumber')
                i.State=request.POST.get('state')
                i.file=request.POST.get('file')
                i.save()
                return render(request,'updateprofile.html')
    return render(request,'updateprofile.html',{'uname':q2})
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

		













# def details(request):
# 		res=signup.objects.filter(Location__contains=location,Name__contains=name1)
# 		if res:
# 			return render(request,'details.html',{"match":res})
		




        # l=[] 
        # loc=signup.objects.all().order_by('Location')
        # for i in loc:
        #     l.append(i.Location)
        # return render(request,'search.html',{'l':l})
# def search1(request):
#     location=request.POST.get('cntry')
#     name1=request.POST.get('searc')
#     city=signup.objects.all()
#     x=0
#     res=signup.objects.filter(Q(Name__iexact=name1 ) and Q(Location__iexact=location))
#     if res:	
#     	return render(request,'search.html',{"match":res})
#     else:
#         messages.error(request, 'no result found')
    




