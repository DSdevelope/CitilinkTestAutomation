from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_detail_page import ProductDetailPage
from pages.products_page import ProductsPage


def test_buy_product():
    """Тест по покупке товара включает
         в себя авторизацию, выбор товара, фильтрация, подтверждение покупки."""
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    print("\nStart Test")
    print("---------------------------------")

    lp = LoginPage(driver)
    mp = MainPage(driver)
    bp = BasketPage(driver)
    pp = ProductsPage(driver)
    dp = ProductDetailPage(driver)

    try:
        lp.authorization()  # Запуск метода авторизации пользователя
    except Exception as e:
        print("Authorization Failed!")
        print(e)

    if mp.basket_is_not_empty():  # Если в корзине есть товары, переходим в неё для очистки
        mp.click_basket_button()
        bp.delete_all_products()
        driver.back()  # Возвращаемся на главную страницу

    mp.select_phones_catalog()  # Переходим в каталог телефонов

    pp.select_product_by_filters()  # Фильтруем товары
    pp.verify_phone_parameters()  # Проверяем параметры товара

    product_name = dp.get_product_name()  # Запоминаем название товара
    product_price = dp.get_product_price()  # Запоминаем цену товара
    dp.buy_product()  # Покупаем товар

    bp.get_and_verify_info(product_name, product_price)  # Получаем данные из корзины и сверяем с полученными при выборе продукта

    print("---------------------------------")
    print("Finish Test")