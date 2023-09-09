import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Client_information_page(Base):
    """Создан класс Client_information_page - страница информации о клиенте, Client_information_page потомок(сын) класса Base"""
    """Класс Client_information_page стал потомком класса Base"""


    def __init__(self, driver):
        """super() используется для вызова метода __init__ родительского класса Base в классе Login_page"""
        super().__init__(driver) # В потомках классов, необязательно прописывать метод init, но он может пригодиться для
        self.driver = driver     # добавления дополнительных атрибутов


    # Locators - локаторы


    first_name = "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    postal_code = "//input[@id='postal-code']"
    continue_button = "//input[@id='continue']"



    # Getters - это метод возвращающий значение некоего свойства класса,  а сеттер(set) соответственно то что устанавливает свойство класса


    def get_first_name(self):
        """Метод get_first_name возвращает нам переменную first_name"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))
    print("get_first_name OK")

    def get_last_name(self):
        """Метод get_last_name возвращает нам переменную last_name"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))
    print("get_last_name Ok")

    def get_postal_code(self):
        """Метод get_postal_code возвращает нам переменную postal_code"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))
    print("get_postal_code OK")

    def get_continue_button(self):
        """Метод get_continue_button возвращает нам переменную continue_button"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))
    print("get_continue_button OK")


    # Actions - действия, Chains - цепочка


    def input_first_name(self, first_name):
        """Создан метод в котором мы будем вводить в поле first_name имя пользователя"""
        self.get_first_name().send_keys(first_name)
        print("Input first_name OK")

    def input_last_name(self, last_name):
        """Создан метод в котором мы будем вводить в поле last_name фамилию пользователя"""
        self.get_last_name().send_keys(last_name)
        print("Input last_name OK")

    def input_postal_code(self, postal_code):
        """Создан метод в котором мы будем вводить в поле postal_code почтовый код"""
        self.get_postal_code().send_keys(postal_code)
        print("input_postal_code OK")

    def click_continue_button(self):
        """Создан метод в котором мы будем кликать на кнопку continue - продолжить"""
        self.get_continue_button().click()
        print("click_continue_button OK")


    # Methods - Вызываем методы


    def input_information(self):
        """Метод input_information вызывает все методы выше"""
        self.get_current_url()
        self.input_first_name("Александр")
        time.sleep(2)
        self.input_last_name("Пислар")
        time.sleep(2)
        self.input_postal_code("+79003625050")
        time.sleep(2)
        self.click_continue_button()
        self.get_screenshot()














