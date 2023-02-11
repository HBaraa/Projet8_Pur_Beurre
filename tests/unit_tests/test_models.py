from django.test import TestCase
from nutella.product.models import Categories, Products


class CategorysTest(TestCase):

    def setUp(self):
        cat = Categories.objects.create(     # noqa
            category="test"
        )

    def test_user(self):
        cat = Categories.objects.get(category="test")
        self.assertEqual(cat.category, "test")


class UserCreationTest(TestCase):

    def setUp(self):
        cat = Categories.objects.create(
            category="test1"
        )
        p = Products(
            name="Product",
            details="Ingredients",
            link="Url",
            image_large="Product_img_l",
            image_small="Product_img_s",
            prod_store="Stores",
            nutriscore="1",
            )

        cat = Categories.objects.get(category="test1")
        p.category = cat
        p.save()

    def test_user(self):
        prod = Products.objects.get(name="Product")
        cat = Categories.objects.get(category="test1")
        self.assertEqual(prod.nutriscore, "1")
        self.assertEqual(prod.details, "Ingredients")
        self.assertEqual(prod.image_large, "Product_img_l")
        self.assertEqual(prod.image_small, "Product_img_s")
        self.assertEqual(prod.prod_store, "Stores")
        self.assertEqual(prod.category, cat)
        self.assertEqual(prod.link, "Url")
