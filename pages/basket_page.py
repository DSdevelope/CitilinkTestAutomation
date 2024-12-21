from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from base.base_class import Base
from utils.logger import Logger


class BasketPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    delete_btn_loc = "//div[@data-meta-name='DeleteAction']"
    name_loc = "//div[@data-meta-name='BasketSnippet']/div/div/a"
    price_loc = "//div[@data-meta-name='AvailableProductStatus__price']/span/span/span"

    # Getters
    def get_product_delete_btn(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.delete_btn_loc)))

    def get_name_label(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.name_loc)))

    def get_price_label(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.price_loc)))

    def get_product_price(self):
        return int(self.get_price_label().text.replace(" ", ""))

    def get_product_name(self):
        return self.get_name_label().text

    # Actions
    def delete_all_products(self):
        try:
            while True:
                self.get_product_delete_btn().click()
                time.sleep(3)
                print("Product Deleted")
                Logger.write_log_to_file("Product Deleted")
        except Exception:
            print("Basket Is Empty")
            Logger.write_log_to_file("Basket Is Empty")

    # Methods
    def get_and_verify_info(self, name: str, price: int):
        Logger.add_start_step("BasketPage: get_and_verify_info")
        self.get_screenshot("basket_page")
        self.assert_url("https://www.citilink.ru/order/")
        assert self.get_product_name() == name
        print("Product Name Assertion OK!")
        Logger.write_log_to_file("Product Name Assertion OK!")
        assert self.get_product_price() == price
        print("Product Price Assertion OK!")
        Logger.write_log_to_file("Product Price Assertion OK!")
        Logger.add_end_step(self.get_current_url(), "BasketPage: get_and_verify_info")
