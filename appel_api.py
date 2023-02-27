import requests
import json
from nutella.product.management.commands import filter


def search():
    r = requests.get(
                    "https://fr.openfoodfacts.org/cgi/search.pl?action=process&search_terms="
                    + "Galettes" +
                    "&sort_by=unique_scans_n&page_size=10&json=1"
                )

    products = json.loads(r.content)
    processed_categories = []
    products_list = products["products"]
    

    print(products_list)


if __name__ == "__main__":
    search()
