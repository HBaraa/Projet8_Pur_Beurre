from django.conf import settings
from django.http import HttpResponse
from django.template import loader
from django.utils.html import escape
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.views import LoginView
from .authentificate import CustomUserAuth as CuA
from django.contrib.auth.decorators import login_required
from .models import CustomUser, CustomUserManager
from . import forms
from .forms import SignUpForm
from .management.commands.insertion import insert_in_data_base
from .models import Products, Categories


# Create your views here.
def home(request):
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")


def mention(request):
    return render(request, "mentionleg.html")


def connect(request):
    return render(request, "connect.html")


class MyLogin(LoginView):
    template_name = "login.html"


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            second_name = form.cleaned_data["second_name"]
            password = form.cleaned_data["password2"]

            user = authenticate(request, username=email, password=password)

            if user == None:
                user = CustomUser.objects.create(
                    password=password,
                    first_name=first_name,
                    second_name=second_name,
                    email=email,
                )
                user.save()

                login(request, user)
            else:
                login(request, user)

            return redirect("http://127.0.0.1:8000/login/")
    else:
        form = SignUpForm()
    return render(request, "signup.html", context={"form": form})


def search_product(request):
    """
    Fonction to search one product in data base.
    """
    query = request.GET.get("query")
    # Query Html escape
    user_product = escape(query)
    print(user_product)
    # Product contains the query is and query is not sensitive to case.
    product = Products.objects.filter(name__icontains=user_product)[:20]
    if not product.exists():
        print("OOOUPS I didn't found it")
    else:
        prod = product[0]
        print(prod)
    print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
    # product = product[0]
    return render(
        request,
        "all_products.html",
        context={
            "product": product,
        },
    )


def product_infos(request, product):

    return render(request, "product_infos.html")
