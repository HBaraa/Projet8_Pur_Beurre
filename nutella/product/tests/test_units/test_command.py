from django.test import TestCase
from io import StringIO
from django.core.management import call_command
import pytest


@pytest.mark.django_db
class TestFillDatabase(TestCase):
    def test_fill_database(self):
        out = StringIO()
        call_command('insertcmnd', stdout=out)
        self.assertIn('Les produits sont, à present, sauvegardées dans la base de données!', out.getvalue())
