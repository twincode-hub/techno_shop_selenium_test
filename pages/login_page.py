from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base


class Login_page(Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    login_field = '//input[@name="USER_LOGIN"]'
    login_field_name = "USER_LOGIN"
    password_field = '//input[@name="USER_PASSWORD"]'
    password_field_name = "USER_PASSWORD"
    # login_button = '//input[@id="login-button"]'
    login_button = '//input[@name="Login"]'
    login_button_name = "Login"
    user_login = 'igor4test'
    user_password = 'igor4test'
    login_word = '//p[contains(text(),"Вы успешно зарегистрировались и авторизовались на сайте!")]'



    #Getters
    def get_login_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.NAME, self.login_field_name)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.NAME, self.password_field_name)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.NAME, self.login_button_name)))

    def get_login_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_word)))


    # Actions

    def clear_login_field(self):
        self.get_login_field().click()
        self.get_login_field().send_keys(Keys.CONTROL + 'a')
        self.get_login_field().send_keys(Keys.DELETE)

    def input_login(self, user_login):
        self.get_login_field().send_keys(user_login)

    def input_password(self, user_password):
        self.get_password_field().send_keys(user_password)

    def click_login_button(self):
        self.get_login_button().click()



    # Methods

    def authorization(self):
        self.clear_login_field()
        self.input_login(self.user_login)
        self.input_password(self.user_password)
        self.click_login_button()
        self.get_screenshot()
        self.assert_word(self.get_login_word(), "Вы успешно зарегистрировались и авторизовались на сайте!")
