from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.views import LoginView
from .authentificate import CustomUserAuth as CuA
from django.contrib.auth.decorators import login_required
from .models import CustomUser, CustomUserManager
from . import forms
from .forms import SignUpForm


# Create your views here.
def home(request):
    return render(request, "home.html")


def connected(request):
    return render(request, "connected.html")


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


def products(request):
    return render(request, "products.html")
