from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    URL = 'https://demowebshop.tricentis.com/'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def go_to_home_page(self):
        self.driver.get(self.URL)

    def wait_until(self, condition, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(condition(locator))
