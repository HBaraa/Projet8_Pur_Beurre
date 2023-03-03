import requests
import responses
from django.core.management import call_command
from django.conf import settings
import pytest
import pprint


def get_items(self):
    response = requests.get(
        f"https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=C%C3%A9r%C3%A9ales%20et%20d%C3%A9riv%C3%A9s&tagtype_1=categories&tag_contains_1=contains&tag_1=C%C3%A9r%C3%A9ales%20et%20d%C3%A9riv%C3%A9s&sort_by=unique_scans_n&page_size=1000&axis_x=energy&axis_y=products_n&action=process&page=2&json=1"
    )
    if response.status_code == 200:
        pprint(response.json()["value"])
        return response.json()
    else:
        return None


@pytest.mark.django_db
@responses.activate
def tests_serch_openfood_failed():
    url = f"https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=C%C3%A9r%C3%A9ales%20et%20d%C3%A9riv%C3%A9s&tagtype_1=categories&tag_contains_1=contains&tag_1=C%C3%A9r%C3%A9ales%20et%20d%C3%A9riv%C3%A9s&sort_by=unique_scans_n&page_size=1000&axis_x=energy&axis_y=products_n&action=process&page=2&json=1"
    responses.add(
        responses.GET,
        url,
        json={"error": "not found"},
        status=404,
    )
    response = get_items(url)
    assert response is None


# @pytest.mark.django_db
# @responses.activate
# def test_search():
#    responses.add(
#        responses.GET,
#        "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=C%C3%A9r%C3%A9ales%20et%20d%C3%A9riv%C3%A9s&tagtype_1=categories&tag_contains_1=contains&tag_1=C%C3%A9r%C3%A9ales%20et%20d%C3%A9riv%C3%A9s&sort_by=unique_scans_n&page_size=1000&axis_x=energy&axis_y=products_n&action=process&page=2&json=1",
#        json={"body": {
#            "id": "2",
#            "name": "Tartines craquantes au blé complet",
#            "details": "Farine de BLÉ complet 55%, farine de BLÉ, farine de MALT de BLÉ, huile de tournesol, sucre, LACTOSÉRUM en poudre, sel. Traces éventuelles de soja.",
#            "link": "https://fr.openfoodfacts.org/produit/3256225722181/tartines-craquantes-au-ble-complet-u",
#            "image_large": "https://images.openfoodfacts.org/images/products/325/622/572/2181/front_fr.60.400.jpg",
#            "image_small": "https://images.openfoodfacts.org/images/products/325/622/572/2181/front_fr.60.200.jpg",
#            "prod_store": "['magasins-u']",
#            "nutriscore": "1",
#            "category_id": "1"
#            }},
#        status=200,
#        )
#    out = StringIO()
#    call_command('insertcmnd', stdout=out)
#    assert Categories.objects.filter(category="Snacks").exists()
