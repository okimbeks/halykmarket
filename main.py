import unittest
from selenium import webdriver
import pytest
from LocatorPage import ObjectPage
from ModulePage import BasePage
from selenium.webdriver.common.by import By

class TestPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        page = BasePage(self.driver)
        self.driver.get(ObjectPage.links["link"])
        self.assertEqual(page.check_title(), "Halyk Market - Выгодные покупки в рассрочку", "Заголовки не совпадают")
        self.assertEqual(page.find_lbl(),True)
        self.assertEqual(page.find_product(),True, "Не найден продукт")
        self.assertEqual(page.compare(), False) # где есть False означает что это негативный кейс/ не совпадание с требованием
        self.assertEqual(page.get_product_price_on_page(), True)
        self.assertEqual(page.active_favorite(),True, "Кнопка избранное недоступна")
        self.assertEqual(page.add_to_fav(), True, "Продукт не добавлен в Избранное")
        self.assertEqual(page.get_price_fav(), True)
        self.assertEqual(page.open_product(), True)
        self.assertEqual(page.compare_title_fav(), True)
        self.assertEqual(page.get_price_on_card(), True)
        self.assertEqual(page.compare_prices(), True)

cls = TestPage()
cls.setUp()




