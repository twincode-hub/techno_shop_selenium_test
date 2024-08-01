import datetime



class Base():

    def __init__(self, driver):
        self.driver = driver


    # main_url = 'https://www.dns-shop.ru/'
    # main_url = 'https://krasnodar.premier-techno.ru/'
    # main_url = 'https://www.saucedemo.com/'
    main_url = 'https://krasnodar.premier-techno.ru/'


    """Method get current URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print('Адрес страницы: ' + get_url)

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Ключевые слова совпадают')


    """Method screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\igor.kochnev\\Documents\\Coding\\Py\\techno_shop_selenium_test\\screen\\' + name_screenshot)
        print('Скриншот выполнен')


    """Method assert URL"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Адрес страницы совпадает')