import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "http://127.0.0.1:8000/"


class TestFunctionnal(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\path\to\chromedriver.exe")
        self.driver.get(BASE_URL)
        self.driver.maximize_window()

    def test_search_prod(self):
        self.driver.get(BASE_URL + "home/")
        self.driver.find_element(By.ID, 'searchForm')
        self.driver.find_element(By.ID, 'searchForm').submit()
        self.assertTrue(self.driver.title == "Pur Beurre for Nutella lovers")
        self.assertTrue(
            self.driver.current_url == "http://127.0.0.1:8000/all_products/?query="
        )

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
