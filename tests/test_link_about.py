import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.Login_page import Login_page
from pages.Main_page import Main_page


def test_link_about():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service(executable_path='D:\\QA_обучениe\\Chrome driver\\chromedriver.exe\\')
    driver = webdriver.Chrome(options=options, service=g)
    print("Start driver OK")

    """Импорт класса Login_page"""
    login = Login_page(driver)
    """Импорт метода из Login_page"""
    login.authorization()

    """Импорт класса Main_page"""
    mp = Main_page(driver)
    mp.select_products_1()

    """Импорт класса Main_page"""
    mp = Main_page(driver)
    mp.select_menu_about()

    time.sleep(2.2)
    driver.quit()










"""С помощью этого кода убираем лишние строки ошибки связанные с сертификатом сайта"""
# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--ignore-ssl-errors')
# driver = webdriver.Chrome(chrome_options=options)