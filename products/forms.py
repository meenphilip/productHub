from django import forms
from .models import Product

# product form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
