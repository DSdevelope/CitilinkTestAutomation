from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utils.logger import Logger


class LoginPage(Base):
    """ Класс содержащий локаторы и методы для страницы Авторизации"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = "https://www.citilink.ru/"
    login = "dstoyanov@list.ru"
    password = "stepik2024"

    # Locators
    register_btn_loc = "//div[@data-meta-name='UserButtonContainer']"
    password_enter_btn_loc = "//button[@class='app-catalog-1oipxdc-Button--StyledSwitcherButton e1e1yge30']"
    login_loc = "//input[@name='login']"
    password_loc = "//input[@name='pass']"
    submit_btn_loc = "//button[@class='e4uhfkv0 app-catalog-1nvnwij e4mggex0']"

    # Getters
    def get_register_btn(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.register_btn_loc)))

    def get_password_enter_btn(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.password_enter_btn_loc)))

    def get_username_field(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.login_loc)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.password_loc)))

    def get_submit_btn(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.submit_btn_loc)))

    # Actions
    def click_register_button(self):
        self.get_register_btn().click()
        print("Click Register Button")
        Logger.write_log_to_file("Click Register Button")

    def click_password_enter_button(self):
        self.get_password_enter_btn().click()
        print("Click Enter With Password Button")
        Logger.write_log_to_file("Click Enter With Password Button")

    def input_login(self, login):
        self.get_username_field().send_keys(login)
        print(f"Input Login '{login}'")
        Logger.write_log_to_file(f"Input Login '{login}'")

    def input_password(self, password):
        self.get_password_field().send_keys(password)
        print(f"Input Password '{password}'")
        Logger.write_log_to_file(f"Input Password '{password}'")

    def click_submit_button(self):
        self.get_submit_btn().click()
        print("Click Submit Button")
        Logger.write_log_to_file("Click Submit Button")

    # Methods
    def authorization(self):
        """ Авторизация в системе"""
        Logger.add_start_step("LoginPage: authorization")
        self.driver.get(self.url)  # открытие требуемой url
        self.click_register_button()
        self.click_password_enter_button()
        self.input_login(self.login)
        self.input_password(self.password)
        self.get_screenshot("login_page")
        self.click_submit_button()
        url = self.get_current_url()
        Logger.add_end_step(url, "LoginPage: authorization")
