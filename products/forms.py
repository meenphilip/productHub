from django import forms
from .models import Product


# product form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Title",
                }
            ),
            "image": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Price",
                }
            ),
            "quantity": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Quantity",
                }
            ),
            "producer": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Producer",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Write description",
                }
            ),
        }
