from django import forms

from .models import Product, Rating


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'stock', 'category']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['stars']