from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product-list"),
    path(
        "product_detail/<int:id>/<slug:slug>/",
        views.product_detail,
        name="product-detail",
    ),
]
