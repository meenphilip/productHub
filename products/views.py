from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.
def product_list(request):
    # get all products
    products = Product.objects.all()
    return render(request, "products/list.html", {"products": products})


# create product detail
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    context = {"product": product}
    return render(request, "products/detail.html", context)
