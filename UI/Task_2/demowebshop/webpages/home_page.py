from selenium.webdriver.common.by import By

from UI.Task_2.demowebshop.webpages.base_page import BasePage


class HomePage(BasePage):
    COMPUTERS_LINK = (By.LINK_TEXT, 'Computers')

    def click_computers(self):
        self.driver.find_element(*self.COMPUTERS_LINK).click()
