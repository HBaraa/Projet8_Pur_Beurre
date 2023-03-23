import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


BASE_URL = "http://127.0.0.1:8000/"


class TestFunctionnal(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\path\to\chromedriver.exe")
        self.driver.get(BASE_URL)
        self.driver.maximize_window()

    def test_search_prod(self):
        self.driver.get(BASE_URL + "home/")
        self.driver.find_element("id", "searchForm")
        self.driver.find_element("id", "searchForm").submit()
        self.assertTrue(self.driver.title == "Pur Beurre for Nutella lovers")
        self.assertTrue(
            self.driver.current_url == "http://127.0.0.1:8000/all_products/?query="
        )

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
