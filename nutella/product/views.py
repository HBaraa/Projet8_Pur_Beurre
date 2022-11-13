from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home.html")


def connected(request):
    return render(request, "connected.html")


def contact(request):
    return render(request, "contact.html")


def mention(request):
    return render(request, "mentionleg.html")
