from selenium.webdriver.common.by import By
class ObjectPage(object):

  links = {
    "link": "https://www.halykmarket.kz/"
  }

  sendkeyslist = {
    "product_name": "iPhone 14 Pro 128 Deep Purple"
  }


  addresses = {
    "1" : (By.CLASS_NAME, "search-input"),
    "2" : (By.XPATH, '/html/body/div[1]/div/div/main/div/div/div/div/div/div/div[2]/div[1]/div/button'),
    "3" : (By.XPATH, '/html/body/div[1]/div/div/main/div/div/div[2]'),
    "4" : (By.XPATH, '//*[@id="__layout"]/div/main/div/div/div[2]/div/div/a')
  }







