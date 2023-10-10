# import time
# import allure
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from pages.Cart_page import Cart_page
# from pages.Client_information_page import Client_information_page
# from pages.Finish_page import Finish_page
# from pages.Login_page import Login_page
# from pages.Main_page import Main_page
# from pages.Payment_page import Payment_page


# @allure.description("Test buy product")  # это некая аннотация, что в отчете было удобно читать и понимать о чем речь
# def test_buy_product():
#     options = webdriver.ChromeOptions()
#     # options.add_argument('--headless')
#     options.add_experimental_option("detach", True)
#     g = Service(executable_path=r"D:\QA_обучение\Chrome_driver\chromedriver.exe")
#     driver = webdriver.Chrome(options=options, service=g)
#     print("Start driver OK")

#     """Импорт класса Login_page"""
#     login = Login_page(driver)
#     """Импорт метода из Login_page"""
#     login.authorization()
#     print("Login page OK")

#     """Импорт класса Main_page"""
#     mp = Main_page(driver)
#     mp.select_products_1()

#     """Импорт класса Cart_page"""
#     cp = Cart_page(driver)
#     cp.product_confirmation()

#     """Импорт класса Client_information_page"""
#     cip = Client_information_page(driver)
#     cip.input_information()

#     """Импорт класса Payment_page"""
#     pp = Payment_page(driver)
#     pp.payment()

#     """Импорт класса Finish_page"""
#     fp = Finish_page(driver)
#     fp.finish()

#     time.sleep(2.2)
#     driver.quit()

