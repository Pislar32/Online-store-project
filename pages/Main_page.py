import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Main_page(Base):
    """Создан класс Main_page -  главная страница, Main_page - потомок(сын) класса Base"""
    """Класс Main_page стал потомком класса Base"""


    def __init__(self, driver):
        """super() используется для вызова метода __init__ родительского класса Base в классе Main_page"""
        super().__init__(driver) # В потомках классов, необязательно прописывать метод init, но он может пригодиться для
        self.driver = driver     # добавления дополнительных атрибутов


    # Locators - локаторы


    select_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    select_product_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    select_product_3 = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    select_product_4 = "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"
    select_product_5 = "//button[@id='add-to-cart-sauce-labs-onesie']"
    select_product_6 = "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"
    cart = "//div[@id='shopping_cart_container']"
    menu = "//button[@id='react-burger-menu-btn']"
    link_about = "//a[@id='about_sidebar_link']"


    # Getters - это метод возвращающий значение некоего свойства класса,  а сеттер(set) соответственно то что устанавливает свойство класса


    def get_select_product_1(self):
        """Метод get_select_product_1 возвращает нам переменную select_product_1"""
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))
    print("Main_page, Select_product_1 OK")

    def get_select_product_2(self):
        """Метод get_select_product_2 возвращает нам переменную select_product_2"""
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))
    print("Main_page, Select_product_2 OK")

    def get_select_product_3(self):
        """Метод get_select_product_3 возвращает нам переменную select_product_3"""
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_product_3)))
    print("Main_page, Select_product_3 OK")

    def get_select_product_4(self):
        """Метод get_select_product_4 возвращает нам переменную select_product_4"""
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_product_4)))
    print("Main_page, Select_product_4 OK")

    def get_select_product_5(self):
        """Метод get_select_product_5 возвращает нам переменную select_product_5"""
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_product_5)))
    print("Main_page, Select_product_5 OK")

    def get_select_product_6(self):
        """Метод get_select_product_6 возвращает нам переменную select_product_6"""
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_product_6)))
    print("Main_page, Select_product_6 OK")

    def get_cart(self):
        """Метод get_cart возвращает нам переменную cart"""
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart)))
    print("Main_page, get_cart OK")

    def get_menu(self):
        """Метод get_menu возвращает нам переменную menu"""
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.menu)))
    print("Main_page, get_menu OK")

    def get_link_about(self):
        """Метод get_link_about возвращает нам переменную link_about"""
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.link_about)))
    print("Main_page, get_link_about OK")


    # Actions - действия, Chains - цепочка


    def click_select_product_1(self):
        """Создан метод в котором мы кликаем на товар №1"""
        self.get_select_product_1().click()
        print("Main_page, click select_product_1 OK")

    def click_select_product_2(self):
        """Создан метод в котором мы кликаем на товар №2"""
        self.get_select_product_2().click()
        print("Main_page, click select_product_2 OK")

    def click_select_product_3(self):
        """Создан метод в котором мы кликаем на товар №3"""
        self.get_select_product_3().click()
        print("Main_page, click select_product_3 OK")

    def click_select_product_4(self):
        """Создан метод в котором мы кликаем на товар №4"""
        self.get_select_product_4().click()
        print("Main_page, click select_product_4 OK")

    def click_select_product_5(self):
        """Execute script - выполнить скрипт"""
        self.driver.execute_script("window.scrollTo(0, 500)")
        print("Scroll select_product_5 passed")
        time.sleep(2)
        """Создан метод в котором мы кликаем на товар №5"""
        self.get_select_product_5().click()
        print("Main_page, click select_product_5 OK")

    def click_select_product_6(self):
        """Execute script - выполнить скрипт"""
        self.driver.execute_script("window.scrollTo(0, 500)")
        print("Scroll select_product_6 passed")
        time.sleep(2)
        """Создан метод в котором мы кликаем на товар №6"""
        self.get_select_product_6().click()
        print("Main_page, click select_product_6 OK")

    def click_cart(self):
        """Создан метод в котором мы кликаем на корзину"""
        self.get_cart().click()
        print("Main_page, click_cart OK")

    def click_menu(self):
        """Создан метод в котором мы кликаем на меню"""
        self.get_menu().click()
    print("Main_page, click_menu OK")

    def click_link_about(self):
        time.sleep(4)
        """Создан метод в котором мы кликаем на кнопку about из меню"""
        action = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, self.link_about)
        action.move_to_element(element).perform() # move - перейти, perform - выполнить
        print("Наведение на элемент выполнено")
        time.sleep(4)
        self.get_link_about().click()
        print("Main_page, click_link_about OK")


    # Methods - Вызываем методы


    def select_products_1(self):
        self.get_current_url()
        time.sleep(2)
        self.click_select_product_1()
        time.sleep(2)
        self.click_cart()

    def select_products_2(self):
        self.get_current_url()
        time.sleep(2)
        self.click_select_product_2()
        time.sleep(2)
        self.click_cart()

    def select_products_3(self):
        self.get_current_url()
        time.sleep(2)
        self.click_select_product_3()
        time.sleep(2)
        self.click_cart()

    def select_products_4(self):
        self.get_current_url()
        time.sleep(2)
        self.click_select_product_4()
        time.sleep(2)
        self.click_cart()

    def select_products_5(self):
        self.get_current_url()
        time.sleep(2)
        self.click_select_product_5()
        time.sleep(2)
        self.click_cart()

    def select_products_6(self):
        self.get_current_url()
        time.sleep(2)
        self.click_select_product_6()
        time.sleep(2)
        self.click_cart()


    def select_menu_about(self):
        self.get_current_url()
        self.click_menu()
        self.click_link_about()
        self.assert_url("https://saucelabs.com/")
















