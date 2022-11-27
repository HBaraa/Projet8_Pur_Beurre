from django.contrib import admin
from .models import Product, Category, Favorite, CustomUser


@admin.register(Product, Category, Favorite, CustomUser)
class GenericAdmin(admin.ModelAdmin):
    pass
