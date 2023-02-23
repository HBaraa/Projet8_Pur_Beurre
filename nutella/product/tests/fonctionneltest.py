import unittest
from selenium import webdriver
from nutella.settings import BASE_DIR
from nutella.product.models import Products, Categories, Favorite, CustomUser
from django.urls import reverse


BASE_URL = "http://127.0.0.1:8000/"


class TestCesiSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path="C:\\browserdrivers\\chromedriver.exe",
        )
        self.driver.maximize_window()

    def test_search_prod(self):
        self.driver.get(BASE_URL + "home/")
        print(self.driver.title)
        self.driver.find_element("id", "searchForm")
        self.driver.find_element("id", "searchForm").submit()
        print(self.driver.current_url)
        self.assertTrue(self.driver.title == 'Pur Beurre for Nutella lovers')
        # self.assertTrue(self.driver.current_url == BASE_URL + 'all_products')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
