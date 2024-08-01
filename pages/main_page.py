from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Main_page(Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators


    # login_button = '//a[@class="logaut"]'
    login_button = '//a[contains(text(),"Войти")]'
    login_button_css = 'a.logaut'
    # login_button = '//span[@class="user-profile__login-icon"]'
    # login_button = '//input[@id="login-button"]'

    #Getters

    def get_login_button(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.login_button_css)))

    #Actions
    def login_button_text(self):
        return self.get_login_button().text

    def login_button_click(self):
        return self.get_login_button().click()


    #Methods
    def need_auth(self):
        self.driver.get(self.main_url)
        self.driver.maximize_window()

        if self.get_login_button().text == "Войти":
            print('Нужна авторизация')
            self.get_login_button().click()
        elif self.get_login_button().text == "Выйти":
            self.get_login_button().click()
        else:
            print('Кнопки для авторизации не обнаружено')

