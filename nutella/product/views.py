from django.urls import reverse
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from .models import Products, CustomUser
from .forms import SignUpForm
from django.contrib.auth import views as auth_views
from .logic_file import (
    found_products,
    search_for_substitute,
    saving_substitute,
    display_favorite,
)
from .models import Products


def home(request):
    return render(request, "home.html")


def accueil(request):
    return render(request, "accueil.html")


def contact(request):
    return render(request, "contact.html")


def history(request):
    return render(request, "history.html")


def mention(request):
    return render(request, "mentionleg.html")


class MyLoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    success_url = "/"


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
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
            login(request, user)
            return redirect(reverse("home"))
        else:
            login(request, user)
            return redirect(reverse("login"))
    else:
        form = SignUpForm()
    return render(request, "signup.html", context={"form": form})


def search_product(request):
    """
    Fonction to search one product in data base.
    """
    query = request.GET.get("query")
    products = found_products(query)
    return render(
        request,
        "all_products.html",
        context={
            "products": products,
        },
    )


def product_infos(request, id):
    product = Products.objects.get(id=id)
    product, substitutes = search_for_substitute(product)
    context = {
        "element": product,
        "substitutes": substitutes,
    }
    return render(request, "product_infos.html", context)


@login_required
def save_favorite(request, id, scndid):
    saving_substitute(request, id, scndid)
    return render(request, "saved_favorite.html")


def display_details(request, id):
    product = Products.objects.get(id=id)
    context = {
        "product": product,
    }
    return render(request, "details.html", context)


@login_required
def favorite(request):
    user = request.user
    context = display_favorite(user)
    return render(request, "favorite.html", context)


@login_required
def moncompte(request):
    return render(request, "moncompte.html")


def logout_view(request):
    logout(request)
    return redirect("login")
