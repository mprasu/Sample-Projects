from django import forms
class LoginForm(forms.Form):
   username = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())

class SendMailForm(forms.Form):
   subject = forms.CharField(label='enter subject',max_length = 100)
   message = forms.CharField(label='enter message',max_length = 100)
   mailid = forms.EmailField(label='enter mailid ')
class ComposeForm(forms.Form):#multiple users
	subject = forms.CharField(initial='enter subject',max_length = 100)
	body = forms.CharField(label='enter message',max_length = 100)
	to = forms.EmailField(label='enter mailid ')
	attachment=forms.CharField(label="enter file to be attached",max_length=100)
