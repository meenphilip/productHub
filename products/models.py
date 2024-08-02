from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="products/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    producer = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-title"]
        indexes = [models.Index(fields=["title"])]

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("product-detail", args=[self.id])
