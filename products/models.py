from django.db import models
from django.utils.text import slugify


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    # slug = models.SlugField(max_length=200, unique_for_year="created_at")
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

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
