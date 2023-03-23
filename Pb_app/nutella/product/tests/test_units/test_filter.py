import json
from django.test import TestCase

from nutella.product.management.filter_file import (
    extract_datas,
    delete_duplicated_products,
)
from nutella.product.management.found_prod import GetDatas


class DownloadProducts(TestCase):
    def test__extract_datas(self):
        with open("fixtures/data_new_fonctionality.json", encoding="utf-8-sig") as f:
            products_data = json.load(f)

        with open(
            "fixtures/data_new_fonctionality_cleaned_data.json", encoding="utf-8-sig"
        ) as f:
            cleaned_products = json.load(f)
        self.assertEqual(
            extract_datas(products_data, "Produits laitiers"), cleaned_products
        )

    def test_eliminate_duplicated_products(self):
        with open("fixtures/data_double.json", encoding="utf-8-sig") as f:
            list_with_double = json.load(f)
        with open("fixtures/double_deleted.json", encoding="utf-8-sig") as f:
            final_list = json.load(f)
            self.assertEqual(delete_duplicated_products(list_with_double), final_list)
