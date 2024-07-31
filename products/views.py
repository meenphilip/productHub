from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm


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


# update product
def product_update(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product-list")
    else:
        form = ProductForm(instance=product)
    context = {"form": form, "product": product}
    return render(request, "products/update.html", context)
