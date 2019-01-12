from django import forms
from .models import *
from django.contrib.auth.models import signup
def clean_username(self):
         user=self.cleaned_data['a1']
         try:
             match=signup.objects.get(Name=user)
         except:
             return self.cleaned_data['a1']
             raise forms.ValidationError("Username already exist")
def clean_email(self):
         email=self.cleaned_data['a3']
         try:
             mt=validate_email(email)
         except:
             return forms.ValidationError("email is not in correct format")
         return email
def clean_confirm_password(self):
         pas=self.cleaned_data['a4']
         cpas=self.cleaned_data['a5']
         MIN_LENGTH=8
         if pas and cpas:
             if pas != cpas:
                 raise forms.ValidationError("Password and confirm password not matched")
             else:
                 if len(pas)< MIN_LENGTH:
                     raise forms.ValidationError("Password should have atleast %d characters" %MIN_LENGTH)
                 if pas.isdigit():
                     raise forms.ValidationError("password should not all numeric")






