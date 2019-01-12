from django.shortcuts import render
from django.views import generic
from django.views import View 
from genericviews.forms import ProductForm
from genericviews.models import Product
from django.views.generic.edit import DeleteView
from django.urls import reverse
from django.shortcuts import get_object_or_404
# normal view to handle the entry of the product and store it on the database
class MakeEntry(View):
    form_class = ProductForm
    template_name = 'makeentry.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            title = request.POST.get('title', '')
            desc = request.POST.get('desc', '')
        prod = Product(title=title, desc=desc)
        prod.save()
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
 
class IndexView(generic.ListView):
    
    context_object_name = 'product_list'
    template_name = 'index.html'
    queryset=Product.objects.all()#standard variable
    
    #def get_queryset(self):
    #return Product.objects.all()
 
class DetailsView(generic.DetailView):
    model = Product
    template_name = 'detail.html'
class DeleteView(DeleteView):
	model=Product
	template_name = "entry_delete.html"
	def get_success_url(self):
		return reverse('index')
