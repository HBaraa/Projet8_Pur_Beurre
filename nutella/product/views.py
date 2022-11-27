from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.views import LoginView
from .authentificate import CustomUserAuth as CuA
from django.contrib.auth.decorators import login_required
from .models import CustomUser
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
    form = forms.SignUpForm()
    if request.method == "POST":
        if form.is_valid():
            return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, "signup.html", context={"form": form})


def products(request):
    return render(request, "products.html")
