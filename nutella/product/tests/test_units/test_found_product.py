from django.conf import settings
import json
import requests
from django.test import TestCase
from management.found_prod import GetDatas
from management.filter_file import extract_datas


class DownloadProducts(TestCase):
    def test_call_openfoodfacts(self):
        with open(
            "fixtures/products_data1.json", encoding="utf-8-sig"
        ) as products_data:
            results_test = json.load(products_data)

        assert GetDatas.all_products == results_test

        with open(
            "fixtures/products_data_eliminate_duplicated.json", encoding="utf-8-sig"
        ) as products_data_eliminated_products:
            results_test = json.load(products_data_eliminated_products)

        self.assertEqual(GetDatas.products_to_inser, results_test)
