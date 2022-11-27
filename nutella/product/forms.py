from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth.validators import UnicodeUsernameValidator


class GetProductForm(forms.Form):
    cherched_product = forms.CharField(label="Produit recherché", max_length=200)


class GetProductChoiceForm(forms.Form):
    chosed_product = forms.CharField(label="produit recherché", max_length=100)


username_validator = UnicodeUsernameValidator()


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)


class Meta:
    model = CustomUser
    fields = ("email", "first_name", "second_name")
