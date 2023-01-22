from .models import CustomUser
from django.contrib.auth.backends import BaseBackend


class CustomUserAuth(object):
    def authenticate(sself, request, username=None, password=None):
        """
        User custom Autentification
        """
        try:
            user = CustomUser.objects.filter(email=username)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None
