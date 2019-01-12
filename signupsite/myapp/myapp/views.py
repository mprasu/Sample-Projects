from django.shortcuts import render,render_to_response
from signup.models import Usersinfo
def hyplink(request):
	l=[]
	for ascii in range(65,90):
		l.append(chr(ascii))
	return render_to_response('hyperlink.html',{'range':l})
def filter_data(request,*args, **kwargs):
	letter=request.GET['query_name'].lower()
	userrecords=Usersinfo.objects.filter(firstname__startswith=letter)
	return render_to_response('filter.html',{'records':userrecords})


#records={}
#	for rec in range(0,len(userrecords)):
#		records.update(userrecords[rec])
	
