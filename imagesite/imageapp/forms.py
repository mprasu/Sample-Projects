from django import forms
class ImageForm(forms.Form):
	name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'style': 'border-color: blue;',
                'placeholder': 'Write your name here'
            }
        )
    )
	image = forms.ImageField()
class SearchForm(forms.Form):
	name=forms.CharField(max_length=30,initial='search')
