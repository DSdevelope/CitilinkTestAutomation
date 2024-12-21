from datetime import datetime


class Base:
    """ Базовый класс, содержащий универсальные методы """

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Метод проверки url"""
        get_url = self.driver.current_url
        print("Сurrent URL: " + get_url)
        return get_url

    def assert_url(self, result):
        """Проверка корректности URL"""
        get_url = self.driver.current_url
        assert result == get_url
        print("URL Assertion OK!")

    def get_screenshot(self, name):
        """Создание скриншота"""
        now_date = datetime.now().strftime("_%Y.%m.%d-%H.%M.%S")
        now_date = ""
        screenshot_name = f"{name}{now_date}.png"
        self.driver.save_screenshot(f"D:\\PROJECTS\\Python\\CitilinkTestAutomation\\screenshots/{screenshot_name}")
        print(f"Screenshot {name} saved")
