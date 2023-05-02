"""
Django settings for nutella project.
Generated by 'django-admin startproject' using Django 4.1.3.
For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from django.conf import settings
import dotenv
import dj_database_url

settings.configure(DEBUG=True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
FIXTURE_DIRS = (os.path.join(BASE_DIR, "fixtures"),)

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# django.setup()
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")
# DJANGO_SETTINGS_MODULE = os.environ.get("DJANGO_SETTINGS_MODULE")

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nutella.settings")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# configurer les serveurs autorisés à accéder à votre app

DATABASES = {}
DATABASES["default"] = dj_database_url.config(conn_max_age=600)

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "pur-beurre.herokuapp.com",
]

# ajout des liens vers les fichiers statiques
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

OPENFOODFACTS_PAGE_SIZE = os.environ.get("OPENFOODFACTS_PAGE_SIZE", 1000)

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "nutella.product",
    "django_fixtures_command",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]


ROOT_URLCONF = "nutella.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR.joinpath("templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "nutella.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES["default"] = dj_database_url.config(conn_max_age=600, ssl_require=True)

CATEGORIE_LIST = [
    "Snacks",
    "Céréales et dérivés",
    "Boissons",
    "Produits laitiers",
    "Pains",
    "Plats préparés",
]


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = ["nutella/product/static/"]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "/home/"
AUTH_USER_MODEL = "product.CustomUser"


AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.ModelBackend"]
