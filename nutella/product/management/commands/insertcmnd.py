﻿import requests
import json
from django.core.management.base import BaseCommand, CommandError

from nutella.product.models import Products, Categories
from .found_prod import GetDatas
from .filter import filter_file


class Command(BaseCommand):
    def handle(self, *args, **options):

        help = "Insert all products an relations in the models tables."

        print("Début de travail!...")

        GetDatas.download_all_products(GetDatas)

        products_to_insert = GetDatas.products_to_inser

        print(
            "Nous avons ",
            len(products_to_insert),
            "produits téléchargées et nettoyées!",
        )

        print("Insértion de tous les produits dans la base de données!")
        cat_list = []
        try:
            for data_dict in products_to_insert:
                c, created = Categories.objects.update_or_create(
                    name=data_dict["category"]
                )
                if data_dict["nutrition_grade_fr"] == "a":
                    nut = 1
                if data_dict["nutrition_grade_fr"] == "b":
                    nut = 2
                if data_dict["nutrition_grade_fr"] == "c":
                    nut = 3
                if data_dict["nutrition_grade_fr"] == "d":
                    nut = 4
                if data_dict["nutrition_grade_fr"] == "e":
                    nut = 5

                # p = Product(
                #    name=data_dict["product_name_fr"],
                #    details=data_dict["ingredients_text_fr"],
                #    link=data_dict["url"],
                #    image_large=data_dict["product_image_large"],
                #    image_small=data_dict["product_image_small"],
                #    prod_store=data_dict["stores"],
                #    nutriscore=nut,
                # )
                prod, obj = Products.objects.update_or_create(
                    name=data_dict["product_name_fr"],
                    details=data_dict["ingredients_text_fr"],
                    code=data_dict["code"],
                    link=data_dict["url"],
                    image_large=data_dict["product_image_large"],
                    image_small=data_dict["product_image_small"],
                    prod_store=data_dict["stores"],
                    nutriscore=nut,
                )
                cat = Categories.objects.filter(name=data_dict["category"]).first()
                prod.category = cat
                prod.save()

        except Exception as e:
            print(e)
            raise CommandError("Ups une erreur est arrivé,")

        self.stdout.write(
            self.style.SUCCESS(
                "Les produits sont, à present, sauvegardées dans la base de données!"
            )
        )
