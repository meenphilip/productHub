from django.contrib import admin
from .models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "quantity", "producer", "slug"]
    list_filter = ["title", "producer", "price"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}
    ordering = ["-title"]
