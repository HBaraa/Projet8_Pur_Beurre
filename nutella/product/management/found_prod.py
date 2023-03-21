import requests
from django.conf import settings
import json
import pprint
from . import filter_file


class GetDatas:
    """
    Class allowing to download and filter the
     products to be inserted in the Data Base.
    """

    all_products = []
    products_to_inser = []

    def __init__(self):
        print("L'importation a commencé, commençons le travail maintenant!")

    def download_all_products(self):
        """
        Fontion to download, clean and parse the products-file.
        """
        # print("Connexion a l'API afin de telecharger les produits")

        for categ in settings.CATEGORIE_LIST:
            r = requests.get(
                        "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0="
                        + str(categ)
                        + "&page_size="
                        + "&json=1"
            )
            try:
                self.current_product = json.loads(r.content)
                self.current_product = filter_file.extract_datas(self.current_product, categ)
                if len(self.current_product) != 0:
                    self.all_products.extend(self.current_product)
                prods = filter_file.delete_duplicated_products(self.all_products)
                self.products_to_inser = prods
            except Exception as e:
                err = e
                pass


if __name__ == "__main__":
    GetDatas()
