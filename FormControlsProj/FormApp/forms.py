from django import forms
#from django.core.exceptions import ValidationError
from FormApp.models import HotelSuprabat

class TestForm(forms.Form):
   roomnumber=forms.ChoiceField(choices=([(rec.pk,rec.roomnumber)for rec in HotelSuprabat.objects.order_by('roomnumber')]))
   roomtype=forms.CharField(max_length=30,required=False)


#((1,'First'),(2,'Second'))