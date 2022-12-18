from django.db import models
from django.db.models import BigAutoField
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


# from django.contrib.auth.models import PermissionsMixin


class Categories(models.Model):
    category = models.TextField(unique=True, null=True)

    def __str__(self):
        return self.category


# Create your models here.
class Products(models.Model):
    name = models.fields.TextField()
    details = models.fields.TextField()
    link = models.URLField(null=True)
    image_large = models.TextField(null=True)
    image_small = models.TextField(null=True)
    prod_store = models.fields.TextField(null=True)
    nutriscore = models.fields.TextField()
    category = models.ForeignKey(
        Categories, verbose_name=_("category"), on_delete=models.CASCADE, null=True
    )

    class Meta:
        db_table = "product"

    def __str__(self):
        return self.name


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    substitute = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="substitute"
    )
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="produit"
    )

    class Meta:
        verbose_name = "Favorite"
        verbose_name_plural = "Favorites"


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with teh given email and password.
        """

        if not email:
            raise ValueError("Vous devez renseigner un email!")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=254, blank=True)
    second_name = models.CharField(max_length=254, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(blank=True, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "second_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
