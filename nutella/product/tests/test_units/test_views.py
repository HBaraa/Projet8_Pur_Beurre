from django.test import TestCase
from django.urls import reverse
from nutella.product.models import Products, Categories, Favorite, CustomUser


class PagesTest(TestCase):
    def test_mentions_legales_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_home_page(self):
        response = self.client.get(reverse("mention"))
        self.assertEqual(response.status_code, 200)

    def test_contact_page(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)

    def test_signup_page(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)

    def test_favorite_page(self):
        response = self.client.get(reverse("favorite"))
        self.assertEqual(response.status_code, 302)

    def test_login_page(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_search_product(self):
        response = self.client.get(reverse("all_products"))
        self.assertEqual(response.status_code, 200)

    def test_product_infos(self):
        categories = Categories.objects.create(                                # noqa
            id=1,
            category="Snacks"
        )
        product = Products.objects.create(
            id=57,
            name="Tartines craquantes au blé complet",
            details="Farine de BLÉ complet 55%, farine de BLÉ, farine de MALT de BLÉ, huile de tournesol, sucre, LACTOSÉRUM en poudre, sel. Traces éventuelles de soja.",
            link="https://fr.openfoodfacts.org/produit/3256225722181/tartines-craquantes-au-ble-complet-u",
            image_large="https://images.openfoodfacts.org/images/products/325/622/572/2181/front_fr.60.400.jpg",
            image_small="https://images.openfoodfacts.org/images/products/325/622/572/2181/front_fr.60.200.jpg",
            prod_store="['magasins-u']",
            nutriscore="1",
            category_id="1"
        )
        response = self.client.get(reverse('product_infos', kwargs={'id': 57}))
        self.assertEqual(response.status_code, 200)

    def test_product_details(self):
        categories = Categories.objects.create(                                # noqa
            id=1,
            category="Snacks"
        )
        product = Products.objects.create(
            id=32,
            name="Pains au lait aux œufs frais",
            details="Farine de _blé_ 56 %, _lait_ écrémé reconstitué 13 %, sucre, œufs_ frais 8,5 %, eau, huile de colza, beurre concentré (_lait_), levure, sel, émulsifiant : mono - et diglycérides d'acides gras et stéaroyl-2-lacrylate de sodium, épaississant : carboxyméthyl-cellulose, arôme (contient alcool), conservateur : propionate de calcium, colorant : caroténoïdes, levure désactivée, anti-oxydant : acide ascorbique",      # noqa
            link="https://fr.openfoodfacts.org/produit/3250390440338/pains-au-lait-aux-oeufs-frais-chabrior",           # noqa
            image_large="https://images.openfoodfacts.org/images/products/325/039/044/0338/front_fr.44.400.jpg",          # noqa
            image_small="https://images.openfoodfacts.org/images/products/325/039/044/0338/front_fr.44.200.jpg",            # noqa
            prod_store="['intermarche']",
            nutriscore="4",
            category_id="1"
        )
        product = Products.objects.get(name="Pains au lait aux œufs frais")
        prod_id = product.id
        response = self.client.post(reverse('product_infos', kwargs={'id': prod_id}))                           # noqa
        self.assertEqual(response.status_code, 200)
