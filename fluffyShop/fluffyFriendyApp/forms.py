
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['placeholder'] = 'Enter URL for the image'

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']