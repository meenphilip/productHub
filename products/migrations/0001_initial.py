# Generated by Django 5.0.7 on 2024-07-31 09:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                ("image", models.ImageField(upload_to="products/")),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("quantity", models.PositiveIntegerField()),
                ("producer", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True)),
            ],
            options={
                "ordering": ["-title"],
                "indexes": [
                    models.Index(fields=["title"], name="products_pr_title_7d8124_idx")
                ],
            },
        ),
    ]
