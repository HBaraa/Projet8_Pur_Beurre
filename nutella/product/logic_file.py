from django.utils.html import escape
from django.urls import reverse
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .models import Products, Favorite, CustomUser
from django.contrib.auth import views as auth_views


def sign_up(form, request):
    email = form.cleaned_data["email"]
    first_name = form.cleaned_data["first_name"]
    second_name = form.cleaned_data["second_name"]
    password = form.cleaned_data["password2"]
    user = authenticate(request, username=email, password=password)
    if user is None:
        user = CustomUser.objects.create_user(
            email=email,
            first_name=first_name,
            second_name=second_name,
            password=password,
        )
    return user


def found_products(query):
    user_product = escape(query)
    print(user_product)
    # Product contains the query is and query is not sensitive to case.
    products = Products.objects.filter(name__icontains=user_product)[:50]
    return products


def search_for_substitute(product):
    nutriscore = product.nutriscore
    substitutes = (
        Products.objects.filter(category_id=product.category)
        .filter(Q(nutriscore__lte=nutriscore))
        .exclude(name=product.name)
        .order_by("nutriscore")
    )[:15]
    return product, substitutes


def saving_substitute(request, id, scndid):
    if request.method == "POST":  # do something with interview_HTML button is clicked
        if request.user.is_authenticated:
            product = Products.objects.get(id=scndid)
            substitute = Products.objects.get(id=id)
            # user_identif = request.user
            favor = Favorite(
                user=request.user,
                product_id=product.id,
                substitute_id=substitute.id,
            )
            favor.save()
            print(product)
            print(id)
            print(product.id)


def display_favorite(user):
    print(user)
    user_id = user.id
    print(user.id)
    # user = CustomUser.objects.get(id=user_id)
    favorites = Favorite.objects.filter(user=user_id)
    context = {"user": user, "favorites": favorites}
    return context
