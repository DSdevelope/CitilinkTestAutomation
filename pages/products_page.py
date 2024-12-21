import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utils.logger import Logger


class ProductsPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    min_price = 10000
    max_price = 65000
    discount = 10

    # Locators
    min_price_filter_loc = "//*[@id='__next']/div/main/section/div[2]/div/div/section/div[1]/div/div/div[2]/div[3]/div/div[3]/div[2]/div[1]/div[2]/div/div[1]/input[1]"
    max_price_filter_loc = "//*[@id='__next']/div/main/section/div[2]/div/div/section/div[1]/div/div/div[2]/div[3]/div/div[3]/div[2]/div[1]/div[2]/div/div[1]/input[2]"
    discount_filter_10plus_loc = "//div[@data-meta-value='10% и больше']"
    memory_filter_256_loc = "//div[@data-meta-value='256 ГБ']"
    color_filter_cyan_loc = "//div[@data-meta-value='голубой']"
    frequency_filter_title_loc = "//div[@data-meta-value='Частота процессора']"
    frequency_filter_2ghz_loc = "//div[@data-meta-value='от 2 ГГц']"
    price_sort_loc = "//button[@data-meta-value='price']"
    price_loc = "(//span[@data-meta-name='Snippet__price'])[1]"
    discount_loc = "(//span[@class='ebsxep70 e9prjkn0 e1b1w42r0 e106ikdt0 app-catalog-rbuprj e1gjr6xo0'])[1]"
    product_name_loc = "(//a[@data-meta-name='Snippet__title'])[1]"

    # Getters
    def get_product_name_link(self):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.product_name_loc)))

    def get_max_price_filter(self):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.max_price_filter_loc)))

    def get_min_price_filter(self):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.min_price_filter_loc)))

    def get_discount_filter(self):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.discount_filter_10plus_loc)))

    def get_memory_filter(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.memory_filter_256_loc)))

    def get_color_filter(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.color_filter_cyan_loc)))

    def get_frequency_title_filter(self):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.frequency_filter_title_loc)))

    def get_frequency_filter_2ghz(self):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.frequency_filter_2ghz_loc)))

    def get_price_sort_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.price_sort_loc)))

    def get_price_label(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.price_loc)))

    def get_discount_label(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.discount_loc)))

    def get_price_value(self):
        return int(self.get_price_label().text[:-1].replace(" ", ""))

    def get_discount_value(self):
        result = ""
        for c in self.get_discount_label().text:
            if c.isdigit():
                result += c
        return int(result)

    # Actions
    def select_discount_filter(self):
        self.get_discount_filter().click()
        print("Select Discount filter 10%")
        Logger.write_log_to_file("Select Discount filter 10%")

    def select_memory_filter(self):
        self.get_memory_filter().click()
        print("Select Memory Filter 256 ГБ")
        Logger.write_log_to_file("Select Memory Filter 256")

    def select_color_filter(self):
        self.get_color_filter().click()
        print("Select Color Filter 'Голубой'")
        Logger.write_log_to_file("Select Color Filter 'Голубой'")

    def select_frequency_filter(self):
        self.get_frequency_title_filter().click()
        time.sleep(1)
        self.get_frequency_filter_2ghz().click()
        print("Select Frequency Filter 2 Ghz")
        Logger.write_log_to_file("Select Frequency Filter 2 Ghz")

    def set_price_filter(self):
        min_price_filter = self.get_min_price_filter()
        min_price_filter.send_keys(Keys.CONTROL + 'a')
        min_price_filter.send_keys(Keys.DELETE)
        min_price_filter.send_keys(str(self.min_price))
        min_price_filter.send_keys(Keys.ENTER)
        print(f"Enter {self.min_price} in Min Price Filter")
        Logger.write_log_to_file(f"Enter {self.min_price} in Min Price Filter")

        max_price_filter = self.get_max_price_filter()
        max_price_filter.send_keys(Keys.CONTROL + 'a')
        max_price_filter.send_keys(Keys.DELETE)
        max_price_filter.send_keys(str(self.max_price))
        max_price_filter.send_keys(Keys.ENTER)
        print(f"Enter {self.max_price} in Max Price Filter")
        Logger.write_log_to_file(f"Enter {self.max_price} in Max Price Filter")

    def click_price_sort_button(self):
        self.get_price_sort_button().click()
        print("Price Sort Button Pressed")
        Logger.write_log_to_file("Price Sort Button Pressed")

    def click_product_name_link(self):
        self.get_product_name_link().click()
        print("Click Product Name Link")
        Logger.write_log_to_file("Click Product Name Link")

    # Methods
    def select_product_by_filters(self):
        time.sleep(2)
        Logger.add_start_step("ProductsPage: select_product_by_filters")
        self.get_screenshot("products_page")
        self.assert_url("https://www.citilink.ru/catalog/smartfony/SAMSUNG/")
        self.driver.execute_script("window.scrollTo(0, 500);")  # Прокрутка к фильтру по цене
        time.sleep(2)
        self.set_price_filter()
        self.driver.execute_script("window.scrollTo(0, 1000);")  # Прокрутка к фильтру скидок
        time.sleep(2)
        self.select_discount_filter()
        self.driver.execute_script("window.scrollTo(0, 2000);")  # Прокрутка к фильтру памяти
        time.sleep(2)
        self.select_memory_filter()
        self.driver.execute_script("window.scrollTo(0, 4200);")  # Прокрутка к фильтру цвета
        time.sleep(2)
        self.select_color_filter()
        self.driver.execute_script("window.scrollTo(0, 5200);")  # Прокрутка к фильтру частоты процессора
        time.sleep(2)
        self.select_frequency_filter()
        Logger.add_end_step(self.get_current_url(), "ProductsPage: select_product_by_filters")

    def verify_phone_parameters(self):
        Logger.add_start_step("ProductsPage: verify_phone_parameters")
        url = self.get_current_url()
        self.driver.execute_script("window.scrollTo(0, 250);")  # Прокрутка к первому товар
        time.sleep(2)
        self.click_price_sort_button()  # Сортировка цены по возрастанию
        time.sleep(2)
        assert self.get_price_value() >= self.min_price  # Убеждаемся, что самая низкая цена не меньше минимально установленной
        self.click_price_sort_button()  # Сортировка цены по убыванию
        time.sleep(2)
        assert self.get_price_value() <= self.max_price  # Убеждаемся, что самая высокая цена не больше максимально установленной
        print("Price Range Assertion OK!")
        Logger.write_log_to_file("Price Range Assertion OK!")
        assert self.get_discount_value() >= self.discount  # Убеждаемся, что скидка не меньше установленной в фильтре
        print("Discount Value Assertion OK!")
        Logger.write_log_to_file("Discount Value Assertion OK!")
        self.click_product_name_link()
        Logger.add_end_step(url, "ProductsPage: verify_phone_parameters")
        time.sleep(2)

