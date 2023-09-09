import datetime


class Base():
    """Созадан класс Base - основной главный класс"""

    def __init__(self, driver):
        """Создан метод инициализации который хранит в себе экземпляр драйвера хром"""
        self.driver = driver


    """Method Get current URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current URL " + get_url) # это свойство объекта driver в Selenium, которое возвращает текущий URL страницы, которую открыл браузер.


    """Method assert word - метод проверки слова"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Assert value_word OK, (Products)")


    """Method get_screenshot - метод скриншота последней страницы"""
    def get_screenshot(self):
        now_date_time = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screen = "screen" + now_date_time + ".png"
        self.driver.save_screenshot("D:\\QA_обучение\\Final_Progect\\screen\\" + name_screen)

        # скрин по времени ПК now_date = datetime.datetime.today().strftime("%Y.%m.%d.%H.%M.%S")
        # date_now = datetime.now().strftime("%Y.%m.%d %H.%M.%S")

    """Method assert_url - метод сравнивает текущую url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("assert value_url OK")










