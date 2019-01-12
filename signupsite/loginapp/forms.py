from django import forms
from signup.models import Usersinfo
from django.core.exceptions import ValidationError
class LoginForm(forms.Form):
   email=forms.CharField(max_length=30,label="MailID :",widget=forms.TextInput(attrs={'placeholder':'Enter your mailid '}))
   password=forms.CharField(label="Password :",max_length=30,widget = forms.PasswordInput(attrs={'placeholder':'Enter your password '}))
        
   def clean_password(self):
            mail=self.cleaned_data.get('email')
            pwd=self.cleaned_data.get('password')
            res=Usersinfo.objects.filter(mailid=mail)
            if res.count()==0:	
                raise ValidationError("could not find your account")
            elif res[0].password!=pwd:
                raise ValidationError("have you forgatten your password")
                  


