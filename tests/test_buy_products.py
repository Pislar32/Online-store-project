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


@pytest.mark.run(order=2) # очередность запуска тестов
def test_buy_product_1(set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service(executable_path='D:\\QA_обучениe\\Chrome driver\\chromedriver.exe\\')
    driver = webdriver.Chrome(options=options, service=g)
    print("Start driver OK")

    """Импорт класса Login_page"""
    login = Login_page(driver)
    login.authorization()

    """Импорт класса Main_page"""
    mp = Main_page(driver)
    mp.select_products_1()

    """Импорт класса Cart_page"""
    cp = Cart_page(driver)
    cp.product_confirmation()

    """Импорт класса Client_information_page"""
    cip = Client_information_page(driver)
    cip.input_information()

    """Импорт класса Payment_page"""
    pp = Payment_page(driver)
    pp.payment()

    """Импорт класса Finish_page"""
    fp = Finish_page(driver)
    fp.finish()

    time.sleep(1.2)
    driver.quit()


@pytest.mark.run(order=1)
def test_buy_product_2():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service(executable_path='D:\\QA_обучениe\\Chrome driver\\chromedriver.exe\\')
    driver = webdriver.Chrome(options=options, service=g)
    print("Start driver OK")

    """Импорт класса Login_page"""
    login = Login_page(driver)
    """Импорт метода из Login_page"""
    login.authorization()
    print("Login page OK")

    """Импорт класса Main_page"""
    mp = Main_page(driver)
    mp.select_products_2()

    """Импорт класса Cart_page"""
    cp = Cart_page(driver)
    cp.product_confirmation()

    """Импорт класса Client_information_page"""
    cip = Client_information_page(driver)
    cip.input_information()

    """Импорт класса Payment_page"""
    pp = Payment_page(driver)
    pp.payment()

    """Импорт класса Finish_page"""
    fp = Finish_page(driver)
    fp.finish()

    time.sleep(1.2)
    driver.quit()


def test_buy_product_3():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service(executable_path='D:\\QA_обучениe\\Chrome driver\\chromedriver.exe\\')
    driver = webdriver.Chrome(options=options, service=g)
    print("Start driver OK")

    """Импорт класса Login_page"""
    login = Login_page(driver)
    """Импорт метода из Login_page"""
    login.authorization()
    print("Login page OK")

    """Импорт класса Main_page"""
    mp = Main_page(driver)
    mp.select_products_3()

    """Импорт класса Cart_page"""
    cp = Cart_page(driver)
    cp.product_confirmation()

    """Импорт класса Client_information_page"""
    cip = Client_information_page(driver)
    cip.input_information()

    """Импорт класса Payment_page"""
    pp = Payment_page(driver)
    pp.payment()

    """Импорт класса Finish_page"""
    fp = Finish_page(driver)
    fp.finish()

    time.sleep(1.2)
    driver.quit()


def test_buy_product_4():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service(executable_path='D:\\QA_обучениe\\Chrome driver\\chromedriver.exe\\')
    driver = webdriver.Chrome(options=options, service=g)
    print("Start driver OK")

    """Импорт класса Login_page"""
    login = Login_page(driver)
    """Импорт метода из Login_page"""
    login.authorization()
    print("Login page OK")

    """Импорт класса Main_page"""
    mp = Main_page(driver)
    mp.select_products_4()

    """Импорт класса Cart_page"""
    cp = Cart_page(driver)
    cp.product_confirmation()

    """Импорт класса Client_information_page"""
    cip = Client_information_page(driver)
    cip.input_information()

    """Импорт класса Payment_page"""
    pp = Payment_page(driver)
    pp.payment()

    """Импорт класса Finish_page"""
    fp = Finish_page(driver)
    fp.finish()

    time.sleep(1.2)
    driver.quit()


def test_buy_product_5():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service(executable_path='D:\\QA_обучениe\\Chrome driver\\chromedriver.exe\\')
    driver = webdriver.Chrome(options=options, service=g)
    print("Start driver OK")

    """Импорт класса Login_page"""
    login = Login_page(driver)
    """Импорт метода из Login_page"""
    login.authorization()
    print("Login page OK")

    """Импорт класса Main_page"""
    mp = Main_page(driver)
    mp.select_products_5()

    """Импорт класса Cart_page"""
    cp = Cart_page(driver)
    cp.product_confirmation()

    """Импорт класса Client_information_page"""
    cip = Client_information_page(driver)
    cip.input_information()

    """Импорт класса Payment_page"""
    pp = Payment_page(driver)
    pp.payment()

    """Импорт класса Finish_page"""
    fp = Finish_page(driver)
    fp.finish()

    time.sleep(1.2)
    driver.quit()


def test_buy_product_6():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service(executable_path='D:\\QA_обучениe\\Chrome driver\\chromedriver.exe\\')
    driver = webdriver.Chrome(options=options, service=g)
    print("Start driver OK")

    """Импорт класса Login_page"""
    login = Login_page(driver)
    """Импорт метода из Login_page"""
    login.authorization()
    print("Login page OK")

    """Импорт класса Main_page"""
    mp = Main_page(driver)
    mp.select_products_6()

    """Импорт класса Cart_page"""
    cp = Cart_page(driver)
    cp.product_confirmation()

    """Импорт класса Client_information_page"""
    cip = Client_information_page(driver)
    cip.input_information()

    """Импорт класса Payment_page"""
    pp = Payment_page(driver)
    pp.payment()

    """Импорт класса Finish_page"""
    fp = Finish_page(driver)
    fp.finish()

    time.sleep(1.2)
    driver.quit()

