from django.utils.html import escape
from django.urls import reverse
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .management.commands.insertion import insert_in_data_base
from .models import Products, Favorite, CustomUser
from django.contrib.auth import views as auth_views


def home(request):
    user = request.user
    if user.is_authenticated:
        print("Déjà connecté")
        print(user.email)
    else:
        print("Please Connect")
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")


def mention(request):
    return render(request, "mentionleg.html")


def connect(request):
    return render(request, "connect.html")


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


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, "****", password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect("home")
        else:
            print("non connected")
            return redirect("login")
    else:
        return render(request, "accounts/login.html")


def search_product(request):
    """
    Fonction to search one product in data base.
    """
    query = request.GET.get("query")
    # Query Html escape
    user_product = escape(query)
    print(user_product)
    # Product contains the query is and query is not sensitive to case.
    products = Products.objects.filter(name__icontains=user_product)[:50]
    return render(
        request,
        "all_products.html",
        context={
            "products": products,
        },
    )


def product_infos(request, id):
    product = Products.objects.get(id=id)
    print("*********************************************")
    print(type(product))
    print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
    nutriscore = product.nutriscore
    substitutes = (
        Products.objects.filter(category_id=product.category)
        .filter(Q(nutriscore__lte=nutriscore))
        .exclude(name=product.name)
        .order_by("nutriscore")
    )[:15]
    context = {
        "element": product,
        "substitutes": substitutes,
    }
    return render(request, "product_infos.html", context)


@login_required
def save_favorite(request, id, scndid):
    if request.method == "POST":  # do something with interview_HTML button is clicked
        if request.user.is_authenticated:
            print("=========================================================")
            product = Products.objects.get(id=scndid)
            substitute = Products.objects.get(id=id)
            print(substitute.id)
            print("22222222222222222222222222222222222222222222222222222222222")
            user_identif = request.user
            print(user_identif)
            print(user_identif.id, product.id, substitute.id)
            favor = Favorite(
                user=request.user,
                product_id=product.id,
                substitute_id=substitute.id,
            )
            favor.save()
            print("YOUUUUUUUUUUUUUUUUUUUUPYYYYYYYYYYYY!!!!!!!!!!!!!!!!!!!!!!!")
            print(product)
            print(id)
            print(product.id)
        else:
            print("connexion deniyed////////////////////////////////")
    return render(request, "saved_favorite.html")


# def save_favorite(request):
#    if request.method == "POST":
#        user = request.user
#        user_id = user.id
#        custom = CustomUser.objects.filter(user=user_id)
#        product = request.POST.get("element")
#        substitute = request.POST.get("x")
#        favor = Favorite(
#            user_id=custom,
#            product_id=product,
#          substitute_id=substitute,
#        )
#        favor.save()
#    return redirect(reverse("product_infos.html"))


@login_required
def favorite(request):
    user = request.user
    print(user)
    user_id = user.id
    print(user.id)
    # user = CustomUser.objects.get(id=user_id)
    favorites = Favorite.objects.filter(user=user_id)
    context = {"user": user, "favorites": favorites}
    return render(request, "favorite.html", context)


@login_required
def moncompte(request):
    return render(request, "moncompte.html")


def logout_view(request):
    logout(request)
    return redirect("home")
