from django.shortcuts import render
from imageapp.forms import ImageForm,SearchForm
# Create your views here.
from imageapp.models import ExampleModel
#from django.http import HttpResponse
from django.shortcuts import redirect
def upload_pic(request):
	if request.method == 'POST':
		form = ImageForm(request.POST,request.FILES)
		if form.is_valid():
			nm=form.cleaned_data['name']
			pic=request.FILES['image']
			m = ExampleModel(name=nm,model_pic=pic)
			m.save()
			img="uploaded succ..."
			return render(request,'imageview.html',{'img':img})
		else:
			return redirect('/image/')
	else:
		form=ImageForm()
		return render(request,"image.html",{"form":form})
def display(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			name=form.cleaned_data['name']
			rec=ExampleModel.objects.filter(name__startswith=name)
			return render(request,'display.html',{"records":rec})
	else:
		form = SearchForm(request.POST)
		return render(request,'search.html',{'form':form})

		
 

