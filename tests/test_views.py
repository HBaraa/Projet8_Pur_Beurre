from django.test import TestCase
from django.urls import reverse


class PagesTest(TestCase):

    def test_mentions_legales_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page(self):
        response = self.client.get(reverse('mention'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_signup_page(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)

    def test_favorite_page(self):
        response = self.client.get(reverse('favorite'))
        self.assertEqual(response.status_code, 302)

    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_search_product(self):
        response = self.client.get(reverse('all_products'))
        self.assertEqual(response.status_code, 200)

