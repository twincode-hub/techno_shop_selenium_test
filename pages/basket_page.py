from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class Basket_page(Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    basket_order_button = '//input[@id="basketOrderButton2"]'
    basket_product_name = '//*[@id="wrap"]/div[5]/div[1]/form/div[1]/div[1]/div[2]/table/tbody/tr/td/a/b'
    basket_total_price = '//div[@class="basket-total-price"]'
    basket_delivery_town_radio = '//input[@id="reKRS"]'
    basket_delivery_price = '//span[@class="bx-soa-cart-d"]'
    basket_cardpay_checkbox = '//input[@id="ID_PAY_SYSTEM_ID_16"]'
    basket_email_input = '//input[@id="soa-property-4"]'
    basket_fio_input = '//input[@id="soa-property-5"]'
    basket_phone_input = '//input[@id="soa-property-6"]'
    basket_order_description_text = '//textarea[@id="orderDescription"]'
    basket_order_go_button = '//a[@id="order_butt_main"]'

    test_mail = 'a@a.ru'
    test_fio = 'Igor Tester'
    test_phone = '79289287928'


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

    def get_basket_cardpay_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_cardpay_checkbox)))

    def get_basket_email_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_email_input)))

    def get_basket_fio_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_fio_input)))

    def get_basket_phone_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_phone_input)))

    def get_basket_order_description_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_order_description_text)))

    def get_basket_order_go_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_order_go_button)))


    #Actions

    def checkout_order(self):
        self.get_basket_delivery_town_radio().click()

        ActionChains(self.driver).move_to_element(self.get_basket_cardpay_checkbox()).perform()
        self.get_basket_cardpay_checkbox().click()

        ActionChains(self.driver).move_to_element(self.get_basket_email_input()).perform()
        self.get_basket_email_input().send_keys(self.test_mail)

        ActionChains(self.driver).move_to_element(self.get_basket_fio_input()).perform()
        self.get_basket_email_input().send_keys(self.test_fio)

        ActionChains(self.driver).move_to_element(self.get_basket_phone_input()).perform()
        self.get_basket_email_input().send_keys(self.test_phone)

        ActionChains(self.driver).move_to_element(self.get_basket_order_go_button()).perform()
        print('basket_order_go_button ready')


    #Methods
    def basket_buy_product(self):
        print('Сравниваем цену товара с итоговой ценой доставки')
        self.assert_word(self.get_basket_total_price(), self.get_basket_delivery_price())
        self.checkout_order()
        self.get_screenshot()




