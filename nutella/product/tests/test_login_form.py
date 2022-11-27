from django.test import TestCase
from django.contrib.auth.models import User


class TestLogin(TestCase):
    def test_login(self):
        user = User.objects.create(username="pablo")
        user.set_password("test")

        response = self.client.post(
            "/login", data={"username": "baraa", "password": "sfsfsfff.4"}
        )

        self.assertEquals(response.status_code, 301)
