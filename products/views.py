from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib import messages
from .models import Product
from .forms import ProductForm


# Create your views here.
def product_list(request):
    # perform a search
    query = request.GET.get("q", "")
    # get all products
    product_list = Product.objects.all()
    # search query
    if query:
        product_list = product_list.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(producer__icontains=query)
        )
    # Pagination with 2 products per page
    paginator = Paginator(product_list, 5)
    page_number = request.GET.get("page")

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer deliver the first page
        products = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        products = paginator.page(paginator.num_pages)

    context = {"products": products, "query": query}
    return render(request, "products/list.html", context)


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
            messages.success(request, "product created successfully")
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
            # Redirect to the product detail page
            messages.success(request, "product updated successfully")
            return redirect("product-detail", id=product.id)
    else:
        form = ProductForm(instance=product)
    context = {"form": form, "product": product}
    return render(request, "products/update.html", context)


def product_delete(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        product.delete()
        messages.success(request, "product deleted successfully")
        return redirect("product-list")

    return render(request, "products/delete.html", {"product": product})
