from django.apps import apps
from django.test import TestCase
from nutella.product.apps import ProductConfig


class ProductsConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(ProductConfig.name, "nutella.product")
        self.assertEqual(apps.get_app_config("product").name, "nutella.product")  # noqa
