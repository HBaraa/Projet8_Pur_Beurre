import pytest

from django.urls import reverse
from django.test import Client
from django.contrib import auth


@pytest.mark.django_db
def test_login_route():

    client = Client()

# Inscrire un utilisateur à l’aide de la vue `signup`afin de l’enregistrer dans la base de données   # noqa
    costum = {
        "email": "colettebaraa@purbeurre.com",
        "first_name": "baraa",
        "last_name": "colette",
        "password1": "sfsfsfff.4",
        "password2": "sfsfsfff.4",
    }
    temp_user = client.post(reverse('signup'), costum)   # noqa
    # Connecter cet utilisateur avec la vue `login`
    response = client.post(reverse('login'), {'username': 'colettebaraa@purbeurre.com', 'password': 'sfsfsfff.4'})  # noqa

    # Vérifier que la redirection vers la page d’accueil est effectuée
    assert response.status_code == 302
    assert response.url == reverse('home')

    # Vérifier que l’utilisateur est bien authentifié
    user = auth.get_user(client)
    assert user.is_authenticated
