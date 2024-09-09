from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from UI.Task_2.demowebshop.webpages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, 'Email')
    PASSWORD_INPUT = (By.ID, 'Password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'input.button-1.login-button')
    LOGIN_LINK = (By.LINK_TEXT, 'Log in')
    HEADER_LINK = (By.CSS_SELECTOR, '.header-links')

    def click_login_link(self):
        self.driver.find_element(*self.LOGIN_LINK).click()

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_welcome_message(self):
        return self.wait_until(EC.presence_of_element_located, self.HEADER_LINK)

