from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.validators import UnicodeUsernameValidator


username_validator = UnicodeUsernameValidator()


class SignUpForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "second_name")
