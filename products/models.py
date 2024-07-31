from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to="products/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    producer = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["-title"]
        indexes = [models.Index(fields=["title"])]

    def __str__(self):
        return f"{self.title}"
