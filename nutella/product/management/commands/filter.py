def filter_file(file1, file2):
    """
    Filter the file !!
    """
    products = file1["products"]  # reach to the list os the products
    wanted_labels = [
        "product_name_fr",
        "url",
        "ingredients_text_fr",
        "nutrition_grade_fr",
    ]  # list of the labels to search
    print("Faisons du travail de nettoyage sur ", file2, "!")
    processed_products = []

    for product in products:  # the list contains dictionaries
        current_product = {}
        for p_label, p_value in product.items():
            if p_label == "categories":
                current_product.update({"category": file2})
            if p_label == "_id":
                current_product.update({"product": p_value})
            if p_label == "stores_tags":
                if p_value == [] or p_value == "null":
                    current_product.update(
                        {"stores": ["Grandes Surfaces", "Superettes"]}
                    )
                else:
                    current_product.update({"stores": p_value})
            if p_label == "selected_images":
                selected = product["selected_images"]
                if len(selected.keys()) == 3:
                    try:
                        product_image_large = selected["front"]["display"]["fr"]
                        current_product.update(
                            {"product_image_large": product_image_large}
                        )
                        product_image_small = selected["front"]["small"]["fr"]
                        current_product.update(
                            {"product_image_small": product_image_small}
                        )
                        product_image_nutrition_large = selected["nutrition"][
                            "display"
                        ]["fr"]
                        current_product.update(
                            {
                                "product_image_nutrition_large": product_image_nutrition_large
                            }
                        )
                        product_image_nutrition_small = selected["nutrition"]["small"][
                            "fr"
                        ]
                        current_product.update(
                            {
                                "product_image_nutrition_small": product_image_nutrition_small
                            }
                        )
                    except KeyError:
                        pass
            if p_label in wanted_labels:
                if len(p_value) != 0 or p_value != " ":
                    if p_value != "null" or p_value != []:
                        current_product.update({p_label: p_value})
            if len(current_product) == 11:
                if current_product not in processed_products:
                    processed_products.append(current_product)

    return processed_products  # return cleaned file


def eliminate_duplicated_products(file):
    """
    Eliminate duplicated products.
    """
    products = file
    print("On commence le filtrage!!")
    processed_products = []
    for product in products:  # the list contains dictionaries
        if product not in processed_products:
            processed_products.append(product)
    return processed_products  # return cleaned file
