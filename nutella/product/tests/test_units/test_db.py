from django.test import TestCase
import pytest
from nutella.product.models import Categories, Products


@pytest.mark.django_db
class ServiceTests(TestCase):
    def setUp(self):
        self.mock_category = Categories.objects.create(
            id="1",
            category="testcategory",
        )
        self.mock_product = Products.objects.create(
            id="1",
            name="testname",
            details="testbrand",
            link="test/url.com",
            image_large="testimagelarge",
            image_small="testimagesmall",
            prod_store="teststore",
            nutriscore="1",
            category_id="1",
        )

    def test_manage_get_product(self):
        self.assertEqual(self.mock_product.name, "testname")

    def test_insertion_category(self):
        self.assertTrue(Categories.objects.filter(category="testcategory").exists())

    def test_insertion_product(self):
        self.assertTrue(Products.objects.filter(name="testname").exists())

    def test_db_length(self):
        self.assertEqual(Products.objects.filter(name="testname").count(), 1)
