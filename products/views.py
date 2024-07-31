from django.shortcuts import render
from .models import Product


# Create your views here.
def product_list(request):
    # get all products
    products = Product.objects.all()
    return render(request, "products/list.html", {"products": products})
