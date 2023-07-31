from selenium.webdriver.common.by import By
from LocatorPage import ObjectPage as op
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains



class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.price_list= price_list=[]
        self.list_title = list_title=[]

    def check_title(self):
        new_title_name = self.driver.find_element(By.TAG_NAME, 'title').get_attribute("innerHTML")
        return new_title_name

    def find_lbl(self):
         element = WebDriverWait(self.driver,5).until(ec.element_to_be_clickable(op.addresses["1"]))
         element.send_keys(op.sendkeyslist['product_name'])
         ActionChains(self.driver).send_keys(Keys.ENTER).perform()
         time.sleep(2)
         return True
    def find_product(self):

         products_nbm = self.driver.find_element(By.CLASS_NAME, "category-page-amount").get_attribute("innerHTML")
         if products_nbm == '0':
            return False
         else:
            return True
    def compare(self):
        time.sleep(2)
        product_name_on_page = self.driver.find_element(By.CLASS_NAME, "product-card-title").get_attribute("innerHTML")
        if product_name_on_page != op.sendkeyslist['product_name']:
            alert = "Название не совпадает"
            return False
        else:
            alert = "Название продукта -iPhone 14 Pro 128 Deep Purple"
            return True

    def get_product_price_on_page(self):
        product_price_on_page = self.driver.find_element(By.CLASS_NAME, "product-card-value-value").get_attribute("innerHTML")
        product_price_on_page = int(''.join(filter(str.isdigit, product_price_on_page)))
        self.price_list.append(product_price_on_page)
        return True


    def active_favorite(self):
        element = WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(op.addresses["2"]))
        if element:
            element.click()
            return True
    def add_to_fav(self):
        icon_fav = self.driver.find_element(By.CLASS_NAME, "icon-text")
        time.sleep(1)
        icon_fav.click()
        time.sleep(1)
        product_name_on_fav = self.driver.find_element(By.CLASS_NAME, "product-card-title").get_attribute("innerHTML")
        product_name_on_fav = product_name_on_fav.replace(" ", "")

        self.list_title.append(product_name_on_fav)
        return True

    def get_price_fav(self):
        product_price_on_fav = self.driver.find_element(By.CLASS_NAME, "product-card-value-value").get_attribute("innerHTML")
        product_price_on_fav = int(''.join(filter(str.isdigit, product_price_on_fav)))
        self.price_list.append(product_price_on_fav)
        return True


    def open_product(self):
        element = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(op.addresses["4"]))
        element.click()
        time.sleep(3)
        return True

    def compare_title_fav(self):
        product_name_on_card = self.driver.find_element(By.CLASS_NAME, "desc-name").get_attribute("innerHTML")
        time.sleep(3)
        product_name_on_card = product_name_on_card.replace(" ", "")
        self.list_title.append(product_name_on_card)
        list_title = self.list_title

        if list_title[0] != list_title[1]:
            name_differ = "The product name is diffrent in favorite and product page"
            return name_differ
        else:
            return True

    def get_price_on_card(self):
        time.sleep(3)
        product_price_on_card = self.driver.find_element(By.CLASS_NAME, "desc-price-value").get_attribute("innerHTML")
        product_price_on_card = int(''.join(filter(str.isdigit, product_price_on_card)))
        self.price_list.append(product_price_on_card)
        return True
    def compare_prices(self):
        price_list = self.price_list
        a = price_list[0]
        for i in price_list:
            if (i > a):
                price_differ = "The product prices is diffrent in first-page, favorite and product pages"
                return price_differ
        else:
            return True
