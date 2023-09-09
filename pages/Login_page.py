import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Login_page(Base):
    """Создан класс Login page - страница авторизации, Login_page потомок(сын) класса Base"""
    """Класс Login page стал потомком класса Base"""

    base_url = 'https://www.saucedemo.com/'
    list_login = ['standard_user']
    list_password = ['secret_sauce']

    def __init__(self, driver):
        """super() используется для вызова метода __init__ родительского класса Base в классе Login_page"""
        super().__init__(driver) # В потомках классов, необязательно прописывать метод init, но он может пригодиться для
        self.driver = driver     # добавления дополнительных атрибутов


    # Locators - локаторы


    user_name = "//input[@id='user-name']"
    password = "//input[@id='password']"
    login_button = "//input[@id='login-button']"
    main_word = "//span[@class='title']"


    # Getters - это метод возвращающий значение некоего свойства класса,  а сеттер(set) соответственно то что устанавливает свойство класса


    def get_user_name(self):
        """Метод get_user_name возвращает нам переменную user_name"""
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))
    print("User Name OK")

    def get_password(self):
        """Метод get_password возвращает нам переменную password"""
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password)))
    print("Password OK")

    def get_login_button(self):
        """Метод get_login_button возвращает нам переменную login_button"""
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))
    print("Login Button OK")

    def get_main_word(self):
        """Метод get_main_word парсит слово - Product на главной странице, для подтверждение авторизации"""
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))
    print("Main_word OK")


    # Actions - действия, Chains - цепочка


    def input_user_name(self, user_name):
        """Создан метод в котором мы будем вводить в поле user_name имя пользователя"""
        self.get_user_name().send_keys(user_name)
        print("Input user_name")

    def input_password(self, password):
        """Создан метод в котором мы будем вводить в поле password пароль"""
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        """Создан метод в котором мы будем нажимать на кнопку login_button - кнопка авторизации"""
        self.get_login_button().click()
        print("Click login_button")


    # Methods - Вызываем методы


    def authorization(self):
        """Метод authorization вызывает все методы выше"""
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.get_current_url()
        time.sleep(2)
        self.input_user_name(self.list_login)
        time.sleep(2)
        self.input_password(self.list_password)
        time.sleep(2)
        self.click_login_button()
        self.assert_word(self.get_main_word(), "Products") # value_word - значение на странице, result - то, что мы ожидает













