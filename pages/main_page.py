from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utils.logger import Logger


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    basket_btn_loc = "//div[@data-meta-name='BasketButton']"
    basket_counter_loc = "//div[@data-meta-name='BasketButton']/div/div/div"
    catalog_btn_loc = "//a[@data-meta-name='DesktopHeaderFixed__catalog-menu']"
    phones_link_loc = "/html/body/div[5]/div/div/div/div/div/div[5]/div/div/div[2]/div/div[1]/div/div[1]/div/a[1]"
    samsung_link_loc = "//a[@href='/catalog/smartfony--samsung-m/']"

    # Getters
    def get_basket_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_btn_loc)))

    def get_basket_counter(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.basket_counter_loc)))

    def get_catalog_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_btn_loc)))

    def get_phones_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phones_link_loc)))

    def get_samsung_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.samsung_link_loc)))

    # Actions

    def basket_is_not_empty(self):
        try:
            self.get_basket_counter()
            return True
        except Exception:
            return False

    def click_basket_button(self):
        self.get_basket_btn().click()
        print("Click Go To Basket Button")
        Logger.write_log_to_file("Click Go To Basket Button")

    def click_catalog_button(self):
        self.get_catalog_btn().click()
        print("Click Catalog Button")
        Logger.write_log_to_file("Click Catalog Button")

    def click_phones_link(self):
        self.get_phones_link().click()
        print("Click Phones Link Button")
        Logger.write_log_to_file("Click Phones Link Button")

    def click_samsung_link(self):
        self.get_samsung_link().click()
        print("Click Samsung Phones Link Button")
        Logger.write_log_to_file("Click Samsung Phones Link Button")

    # Methods
    def select_phones_catalog(self):
        Logger.add_start_step("MainPage: select_phones_catalog")
        self.get_screenshot("main_page")
        self.click_catalog_button()
        self.click_phones_link()
        self.click_samsung_link()
        Logger.add_end_step(self.get_current_url(), "MainPage: select_phones_catalog")
