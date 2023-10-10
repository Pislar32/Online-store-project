import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.Cart_page import Cart_page
from pages.Client_information_page import Client_information_page
from pages.Finish_page import Finish_page
from pages.Login_page import Login_page
from pages.Main_page import Main_page
from pages.Payment_page import Payment_page
import allure



@allure.description("Test buy product 1") # это некая аннотация, что в отчете было удобно читать и понимать о чем речь
@pytest.mark.run(order=1) # очередность запуска тестов
def test_buy_product_1(set_group):
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_experimental_option("detach", True)
    g = Service(executable_path=r"D:\QA_обучение\Chrome_driver\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=g)
    print("Start driver OK")

    """Класса Login_page - выполнение авторизации на сайте"""
    login = Login_page(driver)
    login.authorization()

    """Класса Main_page - выполнение различных действий с товарами, фильтрами, и т.д"""
    mp = Main_page(driver)
    mp.select_products_1()

    """Класса Cart_page - добавление товаров в корзину"""
    cp = Cart_page(driver)
    cp.product_confirmation()

    """Класса Client_information_page - заполнение клиентской информации"""
    cip = Client_information_page(driver)
    cip.input_information()

    """Класса Payment_page - оплата товара"""
    pp = Payment_page(driver)
    pp.payment()

    """Класса Finish_page - сравнивает url, делаем скриншот последней страницы"""
    fp = Finish_page(driver)
    fp.finish()

    time.sleep(1.2)
    driver.quit()


@allure.description("Test buy product 2") # это некая аннотация, что в отчете было удобно читать и понимать о чем речь
@pytest.mark.run(order=2) # очередность запуска тестов
def test_buy_product_2(set_group):
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_experimental_option("detach", True)
    g = Service(executable_path=r"D:\QA_обучение\Chrome_driver\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=g)
    print("Start driver OK")

    """Класса Login_page - выполнение авторизации на сайте"""
    login = Login_page(driver)
    login.authorization()

    """Класса Main_page - выполнение различных действий с товарами, фильтрами, и т.д"""
    mp = Main_page(driver)
    mp.select_products_2()

    """Класса Cart_page - добавление товаров в корзину"""
    cp = Cart_page(driver)
    cp.product_confirmation()

    """Класса Client_information_page - заполнение клиентской информации"""
    cip = Client_information_page(driver)
    cip.input_information()

    """Класса Payment_page - оплата товара"""
    pp = Payment_page(driver)
    pp.payment()

    """Класса Finish_page - сравнивает url, делаем скриншот последней страницы"""
    fp = Finish_page(driver)
    fp.finish()

    time.sleep(1.2)
    driver.quit()


@allure.description("Test buy product 3") # это некая аннотация, что в отчете было удобно читать и понимать о чем речь
@pytest.mark.run(order=3) # очередность запуска тестов
def test_buy_product_3(set_group):
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_experimental_option("detach", True)
    g = Service(executable_path=r"D:\QA_обучение\Chrome_driver\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=g)
    print("Start driver OK")

    """Класса Login_page - выполнение авторизации на сайте"""
    login = Login_page(driver)
    login.authorization()

    """Класса Main_page - выполнение различных действий с товарами, фильтрами, и т.д"""
    mp = Main_page(driver)
    mp.select_products_3()

    """Класса Cart_page - добавление товаров в корзину"""
    cp = Cart_page(driver)
    cp.product_confirmation()

    """Класса Client_information_page - заполнение клиентской информации"""
    cip = Client_information_page(driver)
    cip.input_information()

    """Класса Payment_page - оплата товара"""
    pp = Payment_page(driver)
    pp.payment()

    """Класса Finish_page - сравнивает url, делаем скриншот последней страницы"""
    fp = Finish_page(driver)
    fp.finish()

    time.sleep(1.2)
    driver.quit()

@allure.description("Test buy product 4") # это некая аннотация, что в отчете было удобно читать и понимать о чем речь
@pytest.mark.run(order=4) # очередность запуска тестов
def test_buy_product_4(set_group):
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_experimental_option("detach", True)
    g = Service(executable_path=r"D:\QA_обучение\Chrome_driver\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=g)
    print("Start driver OK")

    """Класса Login_page - выполнение авторизации на сайте"""
    login = Login_page(driver)
    login.authorization()

    """Класса Main_page - выполнение различных действий с товарами, фильтрами, и т.д"""
    mp = Main_page(driver)
    mp.select_products_4()

    """Класса Cart_page - добавление товаров в корзину"""
    cp = Cart_page(driver)
    cp.product_confirmation()

    """Класса Client_information_page - заполнение клиентской информации"""
    cip = Client_information_page(driver)
    cip.input_information()

    """Класса Payment_page - оплата товара"""
    pp = Payment_page(driver)
    pp.payment()

    """Класса Finish_page - сравнивает url, делаем скриншот последней страницы"""
    fp = Finish_page(driver)
    fp.finish()

    time.sleep(1.2)
    driver.quit()


@allure.description("Test buy product 5") # это некая аннотация, что в отчете было удобно читать и понимать о чем речь
@pytest.mark.run(order=6) # очередность запуска тестов
def test_buy_product_5(set_group):
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_experimental_option("detach", True)
    g = Service(executable_path=r"D:\QA_обучение\Chrome_driver\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=g)
    print("Start driver OK")

    """Класса Login_page - выполнение авторизации на сайте"""
    login = Login_page(driver)
    login.authorization()

    """Класса Main_page - выполнение различных действий с товарами, фильтрами, и т.д"""
    mp = Main_page(driver)
    mp.select_products_5()

    """Класса Cart_page - добавление товаров в корзину"""
    cp = Cart_page(driver)
    cp.product_confirmation()

    """Класса Client_information_page - заполнение клиентской информации"""
    cip = Client_information_page(driver)
    cip.input_information()

    """Класса Payment_page - оплата товара"""
    pp = Payment_page(driver)
    pp.payment()

    """Класса Finish_page - сравнивает url, делаем скриншот последней страницы"""
    fp = Finish_page(driver)
    fp.finish()

    time.sleep(1.2)
    driver.quit()


@allure.description("Test buy product 6") # это некая аннотация, что в отчете было удобно читать и понимать о чем речь
@pytest.mark.run(order=5) # очередность запуска тестов
def test_buy_product_6(set_group):
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_experimental_option("detach", True)
    g = Service(executable_path=r"D:\QA_обучение\Chrome_driver\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=g)
    print("Start driver OK")

    """Класса Login_page - выполнение авторизации на сайте"""
    login = Login_page(driver)
    login.authorization()

    """Класса Main_page - выполнение различных действий с товарами, фильтрами, и т.д"""
    mp = Main_page(driver)
    mp.select_products_6()

    """Класса Cart_page - добавление товаров в корзину"""
    cp = Cart_page(driver)
    cp.product_confirmation()

    """Класса Client_information_page - заполнение клиентской информации"""
    cip = Client_information_page(driver)
    cip.input_information()

    """Класса Payment_page - оплата товара"""
    pp = Payment_page(driver)
    pp.payment()

    """Класса Finish_page - сравнивает url, делаем скриншот последней страницы"""
    fp = Finish_page(driver)
    fp.finish()

    time.sleep(1.2)
    driver.quit()



