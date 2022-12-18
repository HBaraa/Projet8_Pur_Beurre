import requests
import json

from nutella.product.models import Products, Categories
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
            c, created = Categories.objects.update_or_create(
                category=data_dict["category"]
            )
            cat = Categories.objects.get(category=processed_categories[0]).id

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

            prod, obj = Products.objects.update_or_create(
                name=data_dict["product_name_fr"],
                details=data_dict["ingredients_text_fr"],
                link=data_dict["url"],
                image_large=data_dict["product_image_large"],
                image_small=data_dict["product_image_small"],
                prod_store=data_dict["stores"],
                nutriscore=score,
                category_id=cat,
            )
    except Exception as e:
        print(e)

    return Products[0].name
