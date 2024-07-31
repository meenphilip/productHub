from django.contrib import admin
from .models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "quantity", "producer"]
    list_filter = ["title", "producer", "price"]
    search_fields = ["title"]
    ordering = ["-title"]
    # prepopulated_fields = {"slug": ("title",)}
