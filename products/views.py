from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm


# Create your views here.
def product_list(request):
    # get all products
    products = Product.objects.all()
    return render(request, "products/list.html", {"products": products})


# create product detail
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    context = {"product": product}
    return render(request, "products/detail.html", context)


# Create product
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product-list")
    else:
        form = ProductForm()
    context = {"form": form}
    return render(request, "products/create.html", context)


# update product
def product_update(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product-list")
    else:
        form = ProductForm(instance=product)
    context = {"form": form, "product": product}
    return render(request, "products/update.html", context)


def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    
    if request.method == 'POST':
        product.delete()
        return redirect('product-list')
    
    return render(request, 'products/delete.html', {'product': product})
