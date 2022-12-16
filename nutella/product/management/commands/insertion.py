import requests
import json

from nutella.product.models import Product, Category
from .filter import filter_file


def insert_in_data_base(product):

    r = requests.get(
        "https://fr.openfoodfacts.org/cgi/search.pl?action=process&search_terms="
        + product
        + "&sort_by=unique_scans_n&page_size=10&json=1"
    )
    products = json.loads(r.content)
    processed_categories = []
    products_list = products["products"]
    for product in products_list:
        for p_label, p_value in product.items():
            if p_label == "categories":
                categories = p_value.split(",")
                for item in categories:
                    if item not in processed_categories:
                        processed_categories.append(item)

    filtred_elements = filter_file(products, processed_categories[0])

    try:  # insert the products in database
        for data_dict in filtred_elements:
            c = Category(category=processed_categories[0])
            c.save()

            if data_dict["nutrition_grade_fr"] == "a":
                score = 1
            if data_dict["nutrition_grade_fr"] == "b":
                score = 2
            if data_dict["nutrition_grade_fr"] == "c":
                score = 3
            if data_dict["nutrition_grade_fr"] == "d":
                score = 4
            if data_dict["nutrition_grade_fr"] == "e":
                score = 5

            prod = Product(
                name=data_dict["product_name_fr"],
                code=data_dict["code"],
                details=data_dict["ingredients_text_fr"],
                url=data_dict["url"],
                image_large=data_dict["product_image_large"],
                image_small=data_dict["product_image_small"],
                store=data_dict["stores"],
                nutriscore=score,
            )
            print(type(prod))

            cat = Category.objects.get(name=data_dict["category"])
            prod.category = cat
            prod.save()
            print(
                "Produit "
                + prod.product_name_fr
                + " inséré de plus dans la base de données!"
            )
    except:
        print("error")

        product = Product.objects.filter(
            product_name_fr=filtred_elements[0]["product_name_fr"]
        )

        return product[0].product_name_fr
