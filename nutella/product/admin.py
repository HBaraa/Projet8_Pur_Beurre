from django.contrib import admin
from .models import Products, Categories, Favorite, CustomUser


@admin.register(Products, Categories, Favorite, CustomUser)
class GenericAdmin(admin.ModelAdmin):
    pass
