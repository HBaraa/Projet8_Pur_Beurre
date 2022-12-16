import requests
import json
from .filter import (
    filter_file,
    eliminate_duplicated_products,
)


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
        print("Connexion a l'API afin de telecharger les produits")

        categories_list = [
            "Snacks",
            "Céréales et dérivés",
            "Boissons",
            "Produits laitiers",
            "Pains",
            "Plats préparés",
        ]

        for item in categories_list:
            r = requests.get(
                "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0="
                + item
                + "&tagtype_1=categories&tag_contains_1=contains&tag_1="
                + item
                + "&sort_by=unique_scans_n&page_size=1000&axis_x=energy&axis_y=products_n&action=process&page=2&json=1"
            )
            try:
                self.current_product = json.loads(r.content)

                self.current_product = filter_file(self.current_product, item)

                if len(self.current_product) != 0:
                    self.all_products.extend(self.current_product)
                prods = eliminate_duplicated_products(self.all_products)
                self.products_to_inser = prods
            except Exception as e:
                print("*********************")
                print(e)
                print("////////////////////////")


if __name__ == "__main__":
    GetDatas()
