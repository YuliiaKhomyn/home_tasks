from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from UI.Task_2.demowebshop.webpages.base_page import BasePage


class ProductPage(BasePage):
    ITEM_BOX = (By.CSS_SELECTOR, '.item-box')
    ADD_TO_WISHLIST_BUTTON = (By.CSS_SELECTOR, '.add-to-wishlist-button')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.bar-notification.success')

    def go_to_product_page(self, product):
        self.driver.get(f'{self.URL}/{product}')

    def wait_for_item_box(self):
        self.wait_until(EC.presence_of_all_elements_located, self.ITEM_BOX)

    def add_to_wishlist(self):
        self.driver.find_element(*self.ADD_TO_WISHLIST_BUTTON).click()

    def wait_for_success_message(self):
        return self.wait_until(EC.visibility_of_element_located, self.SUCCESS_MESSAGE)
