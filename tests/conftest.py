import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

"""Первый подход, Алекс рекомендует этот"""
@pytest.fixture()
def set_up():  # set_up - устанавливать
    print("Start test")

    yield  # yield - это то что будет происходить до начала теста, авторизация, инициализации и тд.

    print("Finish test")


@pytest.fixture(scope="module")  # scope - масштаб
def set_group():  # set_group - установленный набор
    print("Enter system")
    yield
    print("Exit system")


# """Второй подход, Алекс не рекомендует, но он тоже хорош"""
# @pytest.fixture()
# def set_up_():
#     print("Start test")
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("detach", True)
#     g = Service(executable_path='D:\\QA_обучениe\\Chrome driver\\chromedriver.exe\\')
#     driver = webdriver.Chrome(options=options, service=g)
#     base_url = 'https://www.saucedemo.com/'
#     driver.get(base_url)
#     driver.maximize_window()
#
#     yield
#
#     print("Finish test")

