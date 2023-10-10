from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger
import allure



class Cart_page(Base):
    """Создан класс Cart_page -  страница корзины, Cart_page - потомок(сын) класса Base"""
    """Класс Cart_page стал потомком класса Base"""


    def __init__(self, driver):
        """super() используется для вызова метода __init__ родительского класса Base в классе Main_page"""
        super().__init__(driver) # В потомках классов, необязательно прописывать метод init, но он может пригодиться для
        self.driver = driver     # добавления дополнительных атрибутов



    # Locators - локаторы



    checkout_button = "//button[@id='checkout']"



    # Getters - это метод возвращающий значение некоего свойства класса,  а сеттер(set) соответственно то что устанавливает свойство класса



    def get_checkout_button(self):
        """Метод get_checkout_button возвращает нам переменную checkout_button"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))
    print("Cart_page, get_checkout_button OK")



    # Actions - действия, Chains - цепочка



    def click_checkout_button(self):
        """Создан метод в котором мы кликаем на кнопку checkout_button"""
        self.get_checkout_button().click()
        print("Cart_page, click checkout_button OK")



    # Methods - Вызываем методы



    def product_confirmation(self): # confirmation - подтверждение
        with allure.step("Product confirmation"):
            Logger.add_start_step(method="product_confirmation")
            self.get_current_url()
            self.click_checkout_button()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="product_confirmation")
















