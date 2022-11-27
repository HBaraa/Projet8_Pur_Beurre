from django.test import TestCase
from django.urls import reverse


class AccountsPagesTest(TestCase):
    def test_signup_page(self):

        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
