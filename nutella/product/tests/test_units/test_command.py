from django.test import TestCase
from io import StringIO
from django.core.management import call_command
import pytest
from nutella.product.models import Categories, Products


class TestFillDatabase(TestCase):
    def test_fill_database(self):
        out = StringIO()
        call_command("insertcmnd", stdout=out)
        self.assertIn(
            "Les produits sont, à present, sauvegardées dans la base de données!",
            out.getvalue(),
        )
        # self.assertTrue(Products.objects.filter(category_id="1").exists())
        # self.assertEqual(Products.objects.filter(category_id="1").count(), 4)
