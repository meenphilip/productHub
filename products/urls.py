from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product-list"),
    path("product_create/", views.create_product, name="create"),
    path(
        "product_detail/<int:id>/",
        views.product_detail,
        name="product-detail",
    ),
    path(
        "product_update/<int:id>/",
        views.product_update,
        name="product-update",
    ),
]
