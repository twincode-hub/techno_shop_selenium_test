from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver import Keys
from base.base_class import Base


class Shop_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    # actions = ActionChains()

    audio_video = '//span[contains(text(), "Аудио-")]'
    tv_and_acc_catalog = '//a[contains(text(), "Телевизоры и аксессуары")]'
    tv_catalog = '//a[contains(text(), "Телевизоры")]'
    price_slider_class = 'irs-slider to'
    color_tv_checkbox_id = 'arrFilter_2006_2873943235'
    resolution_checkbox_id = 'arrFilter_1433_2140159024'
    matrix_checkbox_id = 'arrFilter_1436_3732816986'
    diagonal_checkbox_id = 'arrFilter_3767_210536161'
    set_filter_button_id = 'set_filter'
    tv_choice_to_cart = '//a[@class="add2basket item145348"]'
    # tv_choice_to_cart = '//a[@href="/personal/cart/"]'
    show_all_color = '//*[@id="ys_filter_bitronic"]/form/div[2]/div[2]/a/span'
    show_all_resolution = '//*[@id="ys_filter_bitronic"]/form/div[4]/div[2]/a/span'
    show_all_matrix = '//*[@id="ys_filter_bitronic"]/form/div[5]/div[2]/a/span'
    show_all_diagonal = '//*[@id="ys_filter_bitronic"]/form/div[6]/div[2]/a/span'
    background = '/html/body'




    # Getters
    def get_audio_video_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.audio_video)))
    def get_tv_and_acc_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tv_and_acc_catalog)))
    def get_tv_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tv_catalog)))
    def get_price_slider(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, self.price_slider_class)))
    def get_color_tv_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.color_tv_checkbox_id)))
    def get_resolution_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.resolution_checkbox_id)))
    def get_matrix_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.matrix_checkbox_id)))
    def get_diagonal_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.diagonal_checkbox_id)))
    def get_set_filter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.set_filter_button_id)))
    def get_tv_choice_to_cart(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.tv_choice_to_cart)))
    def get_show_all_color(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_all_color)))
    def get_show_all_resolution(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_all_resolution)))
    def get_show_all_matrix(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_all_matrix)))
    def get_show_all_diagonal(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_all_diagonal)))
    def get_background(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.background)))



    # Actions
    def enter_audio_video(self):
        # print(self.get_audio_video_button().text)
        self.get_audio_video_button().click()
    def enter_tv_catalog(self):
        self.get_tv_and_acc_catalog().click()
        self.get_tv_catalog().click()
    def make_tv_filter(self):

        self.get_show_all_color().click()
        ActionChains(self.driver).move_to_element(self.get_color_tv_checkbox()).perform()
        print('Навелись на color_tv_checkbox')
        self.get_color_tv_checkbox().click()
        print('click color_tv_checkbox')

        ActionChains(self.driver).move_to_element(self.get_show_all_resolution()).perform()
        print('Навелись на show_all_resolution')
        self.get_show_all_resolution().click()
        print('click show_all_resolution')
        self.get_resolution_checkbox().click()
        print('click resolution_checkbox')

        ActionChains(self.driver).move_to_element(self.get_show_all_matrix()).perform()
        print('Навелись на show_all_matrix')
        self.get_show_all_matrix().click()
        print('show_all_matrix')
        self.get_matrix_checkbox().click()
        print('matrix_checkbox')

        ActionChains(self.driver).move_to_element(self.get_show_all_diagonal()).perform()
        print('Навелись на show_all_diagonal')
        self.get_show_all_diagonal().click()
        print('click show_all_diagonal')
        self.get_diagonal_checkbox().click()
        print('click diagonal_checkbox')

        ActionChains(self.driver).move_to_element(self.get_set_filter_button()).perform()
        print('Навелись на set_filter_button')
        self.get_set_filter_button().click()
        print('click set_filter_button')


    def add_tv_to_cart(self):

        ActionChains(self.driver).move_to_element(self.get_tv_choice_to_cart()).perform()
        print('Навелись на tv_choice_to_cart')
        self.get_tv_choice_to_cart().click()
        print('click tv_choice_to_cart')




    # Methods
    def select_product(self):
        self.enter_audio_video()
        print('Переходим в каталог телевизоров')
        self.enter_tv_catalog()
        self.make_tv_filter()
        self.get_screenshot()
        self.add_tv_to_cart()
        self.get_screenshot()