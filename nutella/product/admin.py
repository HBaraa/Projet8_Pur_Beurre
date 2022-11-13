from django.contrib import admin
from .models import Product, Category, Favorite


@admin.register(Product, Category, Favorite)
class GenericAdmin(admin.ModelAdmin):
    pass
