from django.contrib import admin
from .models import signup

admin.site.register(signup)
list_display = ['Name','Age','Email_id','Password','ConfirmPassword','Phonenumber','Location','State','Country','Address','file']

# Register your models here.
