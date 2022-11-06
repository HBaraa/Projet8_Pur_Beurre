from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.fields.CharField(max_length=100)
    category = models.fields.CharField(max_length=100)
    nutriscore = models.fields.CharField(max_length=1)
    brands = models.CharField(verbose_name="Marques du produit", max_length=100)  # noqa
    link = models.URLField(unique=True, null=True, blank=True)
    image = models.URLField(null=True, blank=True)
