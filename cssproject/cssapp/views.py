from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

from .models import Usersinfo

def index(request):
    members = Usersinfo.objects.all()
    context = {'members': members}
    return render(request, 'index.html', context)

def create(request):
	member = Usersinfo(firstname=request.POST['firstname'], lastname=request.POST['lastname'],mailid=request.POST['mailid'],password=request.POST['password'])
	member.save()
	return redirect('/crud/')

def edit(request, id):
    members = Usersinfo.objects.get(id=id)
    context = {'members': members}
    return render(request, 'edit.html', context)

def update(request, id):
    member = Usersinfo.objects.get(id=id)
    member.firstname = request.POST['firstname']
    member.lastname = request.POST['lastname']
    member.mailid = request.POST['mailid']
    member.save()
    return redirect('/crud/')

def delete(request, id):
    member = Usersinfo.objects.get(id=id)
    member.delete()
    return redirect('/crud/')
