from django import forms
import re
from django.core.exceptions import ValidationError
from signup.models import Usersinfo
class SignupForm(forms.Form):
	firstname = forms.CharField(max_length=100,widget=forms.TextInput(
            attrs={'placeholder': 'Enter yr first name'}))
	lastname = forms.CharField(max_length=100,widget=forms.TextInput(
            attrs={'placeholder': 'Enter yr lastname'}))
	email = forms.EmailField(max_length=100,widget=forms.TextInput(
            attrs={'placeholder': 'Enter your mailid'}))
	password = forms.CharField(max_length=100,widget = forms.PasswordInput(
            attrs={'placeholder': 'Enter your password'}))
	confirmpassword = forms.CharField(max_length=100,widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter your Confirm password here'}))
	
	def clean_firstname(self):
	  fname=self.cleaned_data.get('firstname')
	  if not fname.isalpha():
	     raise ValidationError("please enter only alphabets")
	  return fname

	def clean_lastname(self):
           fname = self.cleaned_data.get('firstname')
           lname=self.cleaned_data.get('lastname')
           rows = Usersinfo.objects.filter(firstname=fname,lastname=lname)
           if not lname.isalpha():
             raise ValidationError("please enter only alphabets")
           elif(rows.count()):
             raise  ValidationError("User already exists")
           return lname
	def clean_password(self):
	  pwd=self.cleaned_data.get('password')
	  pattern='[a-zA-Z][0-9]+'
	  if not re.search(pattern,pwd):
	     raise ValidationError("please enter atleast one uppercase letter and digit")
	  return pwd

	def clean_confirmpassword(self):
	  password1 = self.cleaned_data.get('password')
	  password2 = self.cleaned_data.get('confirmpassword')
	  if (password1 and password2 and password1 != password2):
	     raise ValidationError("confirm password not match with password")
	  return password2
	def clean_email(self):
          mail=self.cleaned_data.get("email")
          rows=Usersinfo.objects.filter(mailid=mail)
          if rows.count():
            raise ValidationError("mailid already exists")
          return mail
                                 
