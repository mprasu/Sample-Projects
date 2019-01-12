from django import forms
class ProductForm(forms.Form):
    # variable for the title of the product
    title = forms.CharField(label="Title", max_length=100)
    # variable for the description of the product
    desc = forms.CharField(label="Description", max_length=300, help_text="Write a brief of the product.",widget=forms.Textarea)