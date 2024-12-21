from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utils.logger import Logger


class ProductDetailPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    name_loc = "//div[@data-meta-name='ProductHeaderLayout__title']"
    price_loc = "//div[@data-meta-name='PriceBlock__price']/span/span/span[1]"
    add_to_basket_loc = "//button[@data-meta-name='BasketDesktopButton']"
    close_popup_loc = "//button[@data-meta-name='UpsaleBasket__close-popup']"
    go_to_basket_loc = "//div[@data-meta-name='BasketButton']"

    # Getters
    def get_name_label(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.name_loc)))

    def get_price_label(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.price_loc)))

    def get_add_to_basket_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_basket_loc)))

    def get_close_popup_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close_popup_loc)))

    def get_go_to_basket_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_basket_loc)))

    def get_product_price(self):
        return int(self.get_price_label().text.replace(" ", ""))

    def get_product_name(self):
        return self.get_name_label().text

    # Actions
    def click_add_to_basket_button(self):
        self.get_add_to_basket_button().click()
        print("Click Add to Basket Button")
        Logger.write_log_to_file("Click Add to Basket Button")

    def click_close_popup_button(self):
        self.get_close_popup_button().click()
        print("Click Close Popup Button")
        Logger.write_log_to_file("Click Close Popup Button")

    def click_go_to_basket_button(self):
        self.get_go_to_basket_button().click()
        print("Click Go To Basket Button")
        Logger.write_log_to_file("Click Go To Basket Button")

    # Methods
    def buy_product(self):
        Logger.add_start_step("ProductDetailPage: buy_product")
        url = self.get_current_url()
        self.driver.execute_script("window.scrollTo(0, 200);")  # Прокрутка вниз
        self.get_screenshot("selected_phone_details")
        self.click_add_to_basket_button()
        self.click_close_popup_button()
        self.click_go_to_basket_button()
        Logger.add_end_step(url, "ProductDetailPage: buy_product")
