from django.shortcuts import render
from django.views.generic.list import ListView
# Create your views here.
from django.shortcuts import render
import datetime
from django.http import HttpResponse
from .models import suprabat_rooms
from django.views.generic import TemplateView,ListView
# Create your views here.
def currenttime(request):
   ctime=datetime.datetime.now()
   htmldoc="<html><body>current server time:%s</body></html>"%(ctime)
   return HttpResponse(htmldoc)
#class HotelListView(ListView):
#	template_name = 'hotel-list.html'
#	queryset = suprabat_rooms.objects.all()
#	context_object_name = 'hotelrecs'
#	paginate_by=5

class HotelListView(TemplateView):
	template_name = 'hotel-list.html'
	def get_context_data(self, *args, **kwargs):
		return {'hotelrecs':suprabat_rooms.objects.all()}