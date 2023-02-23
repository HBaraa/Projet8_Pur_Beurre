﻿from django.test import TestCase
from nutella.product.models import Products, Categories, Favorite, CustomUser
from django.db.models import Q


class LogicTest(TestCase):

    def test_create_account(self):
        user = CustomUser.objects.create(
            email="colette@purbeurre.com",
            first_name="colette",
            second_name="purbeurre",
            password="kjhkhfkh5",
        )
        self.assertIsInstance(user, CustomUser)

    def test_found_product(self):
        categories = Categories.objects.create(
            id=1,
            category="Snacks"
        )
        prod_1 = Products.objects.create(
            id=43,
            name="Pains au lait aux œufs frais",
            details="Farine de _blé_ 56 %, _lait_ écrémé reconstitué 13 %, sucre, œufs_ frais 8,5 %, eau, huile de colza, beurre concentré (_lait_), levure, sel, émulsifiant : mono - et diglycérides d'acides gras et stéaroyl-2-lacrylate de sodium, épaississant : carboxyméthyl-cellulose, arôme (contient alcool), conservateur : propionate de calcium, colorant : caroténoïdes, levure désactivée, anti-oxydant : acide ascorbique",
            link="https://fr.openfoodfacts.org/produit/3250390440338/pains-au-lait-aux-oeufs-frais-chabrior",
            image_large="https://images.openfoodfacts.org/images/products/325/039/044/0338/front_fr.44.400.jpg",
            image_small="https://images.openfoodfacts.org/images/products/325/039/044/0338/front_fr.44.200.jpg",
            prod_store="['intermarche']",
            nutriscore="4",
            category_id="1"
        )
        prod_2 = Products.objects.create(
            id=45,
            name="Pains croustillant Volkoren",
            details="Farine complète de SEIGLE, levure, sel.",
            link="https://fr.openfoodfacts.org/produit/7300400481700/pain-croustillant-volkoren-wasa",
            image_large="https://images.openfoodfacts.org/images/products/730/040/048/1700/front_fr.56.400.jpg",
            image_small="https://images.openfoodfacts.org/images/products/730/040/048/1700/front_fr.56.200.jpg",
            prod_store="['intermarche', 'carrefour', 'delhaize', 'vomar', 'albert-heijn', 'hoogvliet']",
            nutriscore="1",
            category_id="1"
        )
        prod_3 = Products.objects.create(
            id=14,
            name="Pains au chocolat",
            details="sucre pâte de cacao*, beurre de cacao*, émulsifiant ",
            link="https://fr.openfoodfacts.org/produit/20712587/pains-au-chocolat-maitre-jean-pierre",
            image_large="https://images.openfoodfacts.org/images/products/20712587/front_fr.31.400.jpg",
            image_small="https://images.openfoodfacts.org/images/products/20712587/front_fr.31.200.jpg",
            prod_store="['lidl']",
            nutriscore="5",
            category_id="1"
        )
        element = Products.objects.filter(name__icontains="Pain")[:3]
        self.assertEqual(len(element), 3)

    def test_search_for_substitute(self):
        categories = Categories.objects.create(
            id=1,
            category="Snacks"
        )
        prod_1 = Products.objects.create(
            id=14,
            name="Pains au chocolat",
            details="sucre pâte de cacao*, beurre de cacao*, émulsifiant ",
            link="https://fr.openfoodfacts.org/produit/20712587/pains-au-chocolat-maitre-jean-pierre",
            image_large="https://images.openfoodfacts.org/images/products/20712587/front_fr.31.400.jpg",
            image_small="https://images.openfoodfacts.org/images/products/20712587/front_fr.31.200.jpg",
            prod_store="['lidl']",
            nutriscore="5",
            category_id="1"
        )
        prod_2 = Products.objects.create(
            id=45,
            name="Pains croustillant Volkoren",
            details="Farine complète de SEIGLE, levure, sel.",
            link="https://fr.openfoodfacts.org/produit/7300400481700/pain-croustillant-volkoren-wasa",
            image_large="https://images.openfoodfacts.org/images/products/730/040/048/1700/front_fr.56.400.jpg",
            image_small="https://images.openfoodfacts.org/images/products/730/040/048/1700/front_fr.56.200.jpg",
            prod_store="['intermarche', 'carrefour', 'delhaize', 'vomar', 'albert-heijn', 'hoogvliet']",
            nutriscore="1",
            category_id="1"
        )
        prod_3 = Products.objects.create(
            id=43,
            name="Pains au lait aux œufs frais",
            details="Farine de _blé_ 56 %, _lait_ écrémé reconstitué 13 %, sucre, œufs_ frais 8,5 %, eau, huile de colza, beurre concentré (_lait_), levure, sel, émulsifiant : mono - et diglycérides d'acides gras et stéaroyl-2-lacrylate de sodium, épaississant : carboxyméthyl-cellulose, arôme (contient alcool), conservateur : propionate de calcium, colorant : caroténoïdes, levure désactivée, anti-oxydant : acide ascorbique",
            link="https://fr.openfoodfacts.org/produit/3250390440338/pains-au-lait-aux-oeufs-frais-chabrior",
            image_large="https://images.openfoodfacts.org/images/products/325/039/044/0338/front_fr.44.400.jpg",
            image_small="https://images.openfoodfacts.org/images/products/325/039/044/0338/front_fr.44.200.jpg",
            prod_store="['intermarche']",
            nutriscore="4",
            category_id="1"
        )
        substitutes = (
            Products.objects.filter(category_id="1")
            .filter(Q(nutriscore__lte="5"))
            .exclude(name="Pains au chocolat")
            .order_by("nutriscore")
        )[:2]
        self.assertEqual((substitutes[0], substitutes[1]), (prod_2, prod_3))

    def test_save_substitute(self):
        categories = Categories.objects.create(                                # noqa
            id=1,
            category="Snacks"
        )
        product_1 = Products.objects.create(
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
        product_2 = Products.objects.create(
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
        user = CustomUser.objects.update_or_create(
            email="colette@purbeurre.com",
            first_name="colette",
            second_name="purbeurre",
            password="kjhkhfkh5",
        )
        costumer = CustomUser.objects.get(email="colette@purbeurre.com")
        id = costumer.id
        print(id)
        substitute = Favorite.objects.create(
            user_id=id,
            product_id=product_1.id,
            substitute_id=product_2.id,
        )
        favor = Favorite.objects.filter(user=2)
        self.assertIsInstance(substitute, Favorite)

