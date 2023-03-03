import json
from django.test import TestCase
from nutella.product.management.commands.filter import filter_file
from nutella.product.management.commands.found_prod import GetDatas


class DownloadProducts(TestCase):
    def test_clean_data(self):
        with open("fixtures/data_new_fonctionality.json", encoding="utf-8-sig") as f:
            products_data = json.load(f)

        with open(
            "fixtures/data_new_fonctionality_cleaned_data.json", encoding="utf-8-sig"
        ) as f:
            cleaned_products = json.load(f)

        assert filter_file(products_data, "Produits laitiers") == cleaned_products

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
        assert GetDatas.products_to_inser == results_test


# fake_results = {
#    "id": "1",
#     "name": "Galettes bretonnes",
#    "details": "Farine de _blé_, _beurre_ 29%, sucre, _œufs_, sel marin gris, dorure : poudre de _lait_ écrémé.",
#    "link": "https://fr.openfoodfacts.org/produit/3245390084453/galettes-bretonnes-interdis",
#    "image_large": "https://images.openfoodfacts.org/images/products/324/539/008/4453/front_fr.47.400.jpg",
#    "image_small": "https://images.openfoodfacts.org/images/products/324/539/008/4453/front_fr.47.200.jpg",
#    "prod_store": "['carrefour-market', 'carrefour', 'carrefour-fr']",
#    "nutriscore": "5",
#    "category_id": "1"
# }

# @pytest.mark.django_db
# @patch('management.commands.insertcmnd.results')
# def test_results_message(mock_api):
#    """test the results"""
#    products = Products.objects.filter(name="Galettes bretonnes")
#    for item in products:
#        product_id = item.id
#        message = results(product_id)
#
# del message['this_product']
#        mock_api.message = message
#        assert (fake_results == mock_api.message)
#        assert ("Farine de _blé_, _beurre_ 29%, sucre, _œufs_, sel marin gris, dorure : poudre de _lait_ écrémé." == mock_api.message['details'])
