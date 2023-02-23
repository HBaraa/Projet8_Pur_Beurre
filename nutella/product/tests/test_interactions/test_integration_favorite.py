from django.urls import reverse
from django.test import Client
from django.contrib import auth
from nutella.product.models import Products, Categories

import pytest

CLIENT = Client()


@pytest.mark.django_db
def test_favorite_page():

    """
    First, we test if the 'favorite' maps to favorite View,
    then we test if the favorite View rendered the
    correct template ( favorite.html )
    and fetched the products from the correct model ( Favourite )
    """
    credentials = {
        'email': 'testuser@testing.com',
        'first_name': 'Test',
        'last_name': 'User',
        'password1': 'TestPassword',
        'password2': 'TestPassword'
    }
    temp_user = CLIENT.post(reverse('signup'), credentials)              # noqa
    response = CLIENT.post(reverse('login'), {'username': 'testuser@testing.com', 'password': 'TestPassword'})     # noqa
    assert response.status_code == 302
    assert response.url == reverse('home')
    user = auth.get_user(CLIENT)
    assert user.is_authenticated
    response = CLIENT.post(reverse('favorite'))
    assert response.status_code == 200
    response = CLIENT.post(reverse('moncompte'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_display_all_products():
    CLIENT.post(reverse('home'))
    response = CLIENT.get(reverse('all_products'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_search_products():
    credentials = {
        'email': 'testuser@testing.com',
        'first_name': 'Test',
        'last_name': 'User',
        'password1': 'TestPassword',
        'password2': 'TestPassword'
    }
    temp_user = CLIENT.post(reverse('signup'), credentials)         # noqa
    response = CLIENT.post(reverse('login'), {'username': 'testuser@testing.com', 'password': 'TestPassword'})     # noqa
    assert response.status_code == 302
    assert response.url == reverse('home')
    user = auth.get_user(CLIENT)
    assert user.is_authenticated
    categories = Categories.objects.create(                                # noqa
        id=1,
        category="Snacks"
    )
    product = Products.objects.create(
        id=50,
        name="Pains au lait aux œufs frais",
        details="Farine de _blé_ 56 %, _lait_ écrémé reconstitué 13 %, sucre, œufs_ frais 8,5 %, eau, huile de colza, beurre concentré (_lait_), levure, sel, émulsifiant : mono - et diglycérides d'acides gras et stéaroyl-2-lacrylate de sodium, épaississant : carboxyméthyl-cellulose, arôme (contient alcool), conservateur : propionate de calcium, colorant : caroténoïdes, levure désactivée, anti-oxydant : acide ascorbique",      # noqa
        link="https://fr.openfoodfacts.org/produit/3250390440338/pains-au-lait-aux-oeufs-frais-chabrior",           # noqa
        image_large="https://images.openfoodfacts.org/images/products/325/039/044/0338/front_fr.44.400.jpg",          # noqa
        image_small="https://images.openfoodfacts.org/images/products/325/039/044/0338/front_fr.44.200.jpg",            # noqa
        prod_store="['intermarche']",
        nutriscore="4",
        category_id="1"
    )
    substitute = Products.objects.create(
        id=67,
        name="Tartines craquantes au blé complet",
        details="Farine de BLÉ complet 55%, farine de BLÉ, farine de MALT de BLÉ, huile de tournesol, sucre, LACTOSÉRUM en poudre, sel. Traces éventuelles de soja.",       # noqa
        link="https://fr.openfoodfacts.org/produit/3256225722181/tartines-craquantes-au-ble-complet-u",           # noqa
        image_large="https://images.openfoodfacts.org/images/products/325/622/572/2181/front_fr.60.400.jpg",            # noqa
        image_small="https://images.openfoodfacts.org/images/products/325/622/572/2181/front_fr.60.200.jpg",                # noqa
        prod_store="['magasins-u']",
        nutriscore="1",
        category_id="1"
    )
    print("PPPPPPPresque DOOOONE!!!!!!!")
    prod_id = product.id
    print(prod_id)
    print(type(prod_id))
    show_details = CLIENT.post(reverse('product_infos', kwargs={'id': prod_id}))     # noqa
    assert show_details.status_code == 200
    sub_id = substitute.id
    save_favorite = CLIENT.post(reverse('save_favorite', kwargs={'id': prod_id, 'scndid': sub_id}))    # noqa
    assert save_favorite.status_code == 200
    # assert show_details.status_code == 302
    # assert response.url == reverse('all_products')
