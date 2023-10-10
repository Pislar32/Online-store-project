from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger
import allure


class Finish_page(Base):
    """Создан класс Finish_page -  страница скриншота, Finish_page - потомок(сын) класса Base"""
    """Класс Finish_page стал потомком класса Base"""


    def __init__(self, driver):
        """super() используется для вызова метода __init__ родительского класса Base в классе Main_page"""
        super().__init__(driver) # В потомках классов, необязательно прописывать метод init, но он может пригодиться для
        self.driver = driver     # добавления дополнительных атрибутов


    # Locators - локаторы





    # Getters - это метод возвращающий значение некоего свойства класса,  а сеттер(set) соответственно то что устанавливает свойство класса





    # Actions - действия, Chains - цепочка




    # Methods - Вызываем методы


    def finish(self):
        """Метод screenshot вызывает все методы выше"""
        with allure.step("Finish"):
            Logger.add_start_step(method="finish")
            self.get_current_url()
            self.assert_url("https://www.saucedemo.com/checkout-complete.html")
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="finish")
















