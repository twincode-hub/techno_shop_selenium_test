from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import Login_page
from pages.main_page import Main_page
from base.base_class import Base
from pages.shop_page import Shop_page


def test_buy_product():
    """Драйвер хрома"""
    options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_argument('--headless') # <----- аргумент для запуска теста без открытия браузера (headless режим)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))



    mp = Main_page(driver)
    mp.need_auth()

    login = Login_page(driver)
    login.authorization()

    shop = Shop_page(driver)
    shop.select_product()

