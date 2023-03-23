"""nutella URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from django.conf.urls.static import static
from .product import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", views.MyLoginView.as_view(), name="login"),
    path("pur-beurre.herokuapp.com/", views.home, name="home"),
    path("moncompte/", views.moncompte, name="moncompte"),
    path("contact/", views.contact, name="contact"),
    path("mention/", views.mention, name="mention"),
    path("signup/", views.signup, name="signup"),
    path("all_products/", views.search_product, name="all_products"),
    path("product_infos/<int:id>/", views.product_infos, name="product_infos"),
    path(
        "save_favorite/<int:id> <int:scndid>/",
        views.save_favorite,
        name="save_favorite",
    ),  # noqa
    path("favorite/", views.favorite, name="favorite"),
    path("history/", views.history, name="history"),
    path("logout/", views.logout_view, name="logout"),
    path("details/<int:id>", views.display_details, name="details"),
]
