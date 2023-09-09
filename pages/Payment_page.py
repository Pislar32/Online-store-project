from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Payment_page(Base):
    """Создан класс Payment_page -  страница оплаты, Payment_page - потомок(сын) класса Base"""
    """Класс Payment_page стал потомком класса Base"""


    def __init__(self, driver):
        """super() используется для вызова метода __init__ родительского класса Base в классе Main_page"""
        super().__init__(driver) # В потомках классов, необязательно прописывать метод init, но он может пригодиться для
        self.driver = driver     # добавления дополнительных атрибутов


    # Locators - локаторы


    finish_button = "//button[@id='finish']"



    # Getters - это метод возвращающий значение некоего свойства класса,  а сеттер(set) соответственно то что устанавливает свойство класса


    def get_finish_button(self):
        """Метод get_finish_button возвращает нам переменную finish_button"""
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))
    print("Payment_page, get_finish_button OK")


    # Actions - действия, Chains - цепочка


    def click_finish_button(self):
        """Создан метод в котором мы кликаем на кнопку Finish"""
        self.get_finish_button().click()
        print("Payment_page, click_finish_button OK")


    # Methods - Вызываем методы


    def payment(self):
        """Метод payment вызывает все методы выше"""
        self.get_current_url()
        self.click_finish_button()
        self.get_screenshot()















