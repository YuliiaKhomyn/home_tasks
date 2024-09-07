from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from UI.Task_2.demowebshop.webpages.base_page import BasePage


class RegisterPage(BasePage):
    REGISTER_LINK = (By.LINK_TEXT, 'Register')
    GENDER_MALE_RADIO = (By.ID, 'gender-male')
    FIRST_NAME_INPUT = (By.ID, 'FirstName')
    LAST_NAME_INPUT = (By.ID, 'LastName')
    EMAIL_INPUT = (By.ID, 'Email')
    PASSWORD_INPUT = (By.ID, 'Password')
    CONFIRM_PASSWORD_INPUT = (By.ID, 'ConfirmPassword')
    REGISTER_BUTTON = (By.ID, 'register-button')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.result')

    def click_register_link(self):
        self.driver.find_element(*self.REGISTER_LINK).click()

    def enter_male_gender(self):
        self.driver.find_element(*self.GENDER_MALE_RADIO).click()

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def enter_confirm_password(self, password):
        self.driver.find_element(*self.CONFIRM_PASSWORD_INPUT).send_keys(password)

    def click_confirm_register(self):
        self.driver.find_element(*self.REGISTER_BUTTON).click()

    def get_success_message(self):
        return self.wait_until(EC.presence_of_element_located, self.SUCCESS_MESSAGE)
