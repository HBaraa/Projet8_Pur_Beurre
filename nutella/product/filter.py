def filter_file(data):
    elements = data["products"]  # reach to the list os the products
    searched_labels = [
        "product_name_fr",
        "code",
        "ingredients_text_fr",
        "url",
        "store",
        "nutrition_grade_fr",
    ]  # list of the labels to search
