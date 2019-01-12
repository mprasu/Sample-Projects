from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
# Create your views here.
from .models import Product
class ProductInputView(CreateView):
    model = Product 
    template_name = 'input.html'
    fields='__all__'
 
    def form_valid(self, form):
        model = form.save(commit=False)
	#save & returns model object with out commit mode,
	#so helps us to add some more fields which are not there in model.for example.
        #model.submitted_by = self.request.user
        model.save()
        return HttpResponseRedirect(self.get_success_url())
 
    def get_success_url(self):
        return reverse('ProductsApp:link')

class ProductTemplate(TemplateView):
	template_name='link.html'

class ProductListView(ListView):
	context_object_name = 'records'
	template_name = 'display.html'
	queryset=Product.objects.all()
   
