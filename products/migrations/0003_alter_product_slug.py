# Generated by Django 5.0.7 on 2024-07-31 18:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_product_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="slug",
            field=models.SlugField(max_length=200, unique_for_year="created_at"),
        ),
    ]
