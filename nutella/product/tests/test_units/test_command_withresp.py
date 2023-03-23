import requests
from django.test import TestCase
import responses
import pytest
from django.test import override_settings
from django.core.management import call_command
from io import StringIO


@pytest.mark.django_db
@responses.activate
@override_settings(CATEGORIE_LIST=["Snacks"])
def get_items():
    response = requests.get(
        "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=Snacks&tagtype_1=categories&tag_contains_1=contains&tag_1=Snacks&sort_by=unique_scans_n&page_size=1000&axis_x=energy&axis_y=products_n&action=process&page=2&json=1"
    )
    if response.status_code == 200:
        print(response.json()["value"])
        return response.json()
    else:
        return None


@pytest.mark.django_db
@responses.activate
@override_settings(CATEGORIE_LIST=["Snacks"])
def tests_serch_openfood_failed():
    url = f"https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=Snacks&tagtype_1=categories&tag_contains_1=contains&tag_1=Snacks&sort_by=unique_scans_n&page_size=1000&axis_x=energy&axis_y=products_n&action=process&page=2&json=1"
    responses.add(
        responses.GET,
        url,
        json={"error": "not found"},
        status=404,
    )
    response = get_items()
    assert response is None


class ClosepollTest(TestCase):
    @pytest.mark.django_db
    @responses.activate
    @override_settings(CATEGORIE_LIST=["Snacks"])
    def test_search(self):
        responses.add(
            responses.GET,
            f"https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=Snacks&tagtype_1=categories&tag_contains_1=contains&tag_1=Snacks&sort_by=unique_scans_n&page_size=1000&axis_x=energy&axis_y=products_n&action=process&page=2&json=1",
            json={
                "count": 1,
                "page": 1,
                "page_count": 1,
                "page_size": 1,
                "products": [
                    {
                        "nutriscore_grade": "a",
                        "categories": "Snacks",
                        "ingredients_text_fr": "vitamine D",
                        "url": "https://fr.openfoodfacts.org",
                        "product_image_large": "https://static.openfoodfacts.org/images/products/342/827/398/0046/front_fr.52.400.jpg",
                        "product_image_small": "https://static.openfoodfacts.org/images/products/342/827/398/0046/front_fr.52.200.jpg",
                        "product_image_nutrition_large": "https://static.openfoodfacts.org/images/products/342/827/398/0046/nutrition_fr.96.400.jpg",
                        "product_image_nutrition_small": "https://static.openfoodfacts.org/images/products/342/827/398/0046/nutrition_",
                        "stores": ["Grandes Surfaces", "Superettes"],
                        "product_name_fr": "Cruesli mélange de noix",
                        "product": "1",
                    },
                ],
                "skip": 0,
            },
            status=200,
        )
        out = StringIO()
        call_command("insert_command", stdout=out)
        val = out.getvalue()
        self.assertIn(
            "Les produits sont, à present, sauvegardées dans la base de données!", val
        )
