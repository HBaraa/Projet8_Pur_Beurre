from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


# Create your models here.
class Product(models.Model):
    name = models.fields.CharField(max_length=100)
    code = models.fields.IntegerField()
    details = models.fields.CharField(max_length=1000)
    link = models.URLField(unique=True, null=True)
    image = models.URLField(null=True)
    prod_store = models.fields.CharField(max_length=150, null=True)
    nutriscore = models.fields.CharField(max_length=1)
    categories = models.ManyToManyField("Category", related_name="products")

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    substitute = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="substitute"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="produit"
    )

    class Meta:
        verbose_name = "Favorite"
        verbose_name_plural = "Favorites"
