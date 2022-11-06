from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.fields.CharField(max_length=100)
    category = models.fields.CharField(max_length=1000)
    nutriscore = models.fields.CharField(max_length=1)
