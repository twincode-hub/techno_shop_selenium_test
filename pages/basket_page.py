from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Basket_page(Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    basket_order_button = '//input[@id="basketOrderButton2"]'
    basket_product_name = '//*[@id="wrap"]/div[5]/div[1]/form/div[1]/div[1]/div[2]/table/tbody/tr/td/a/b'
    basket_total_price = '//div[@class="basket-total-price"]'
    basket_delivery_town_radio = '//input[@id="reRND"]'
    basket_delivery_price = '//span[@class="bx-soa-cart-d"]'
    basket_cardpay_checkbox = '//input[@id="ID_PAY_SYSTEM_ID_16"]'
    basket_email_input = '//input[@id="soa-property-4"]'
    basket_fio_input = '//input[@id="soa-property-5"]'
    basket_phone_input = '//input[@id="soa-property-6"]'
    basket_order_description_text = '//textarea[@id="orderDescription"]'


    #Getters
    def get_basket_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_order_button)))

    def get_basket_product_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_product_name)))

    def get_basket_total_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_total_price)))

    def get_basket_delivery_town_radio(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_delivery_town_radio)))

    def get_basket_delivery_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_delivery_price)))





    #Actions


    #Methods




