import requests
from django.conf import settings
import json
import pprint
from nutella.product.models import Products
from nutella.product.management.commands.filter import (
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
                + "&sort_by=unique_scans_n&page_size="
                + str(settings.OPENFOODFACTS_PAGE_SIZE)
                + "&axis_x=energy&axis_y=products_n&action=process&page=2&json=1"
            )
            try:
                self.current_product = json.loads(r.content)
                self.current_product = filter_file(self.current_product, item)
                pprint(self.current_product)
                if len(self.current_product) != 0:
                    self.all_products.extend(self.current_product)
                prods = eliminate_duplicated_products(self.all_products)
                self.products_to_inser = prods
            except Exception as e:
                print(e)


# def results(product_id):
#    """Interprate results"""
#    id = int(product_id)
#    this_product = Products.objects.get(pk=id)
#    message = {
#        "id": this_product.id,
#        "name": this_product.name,
#        "details": this_product.details,
#        "link": this_product.link,
#        "image_large": this_product.image_large,
#        "image_small": this_product.image_small,
#        "prod_store": this_product.prod_store,
#        "nutriscore": this_product.nutriscore,
#        "category_id": this_product.category_id
#    }
#    return message


if __name__ == "__main__":
    GetDatas()
