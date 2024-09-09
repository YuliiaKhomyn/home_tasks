from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from UI.Task_2.demowebshop.webpages.base_page import BasePage


class CartPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-button-5')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.bar-notification.success')
    SHOPPING_CART_LINK = (By.LINK_TEXT, 'Shopping cart')
    CART_ITEMS = (By.CSS_SELECTOR, '.cart-item-row')
    REMOVE_CHECKBOX = (By.NAME, 'removefromcart')
    UPDATE_CART_BUTTON = (By.NAME, 'updatecart')
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, '.order-summary-content')

    def add_item_to_cart(self):
        add_to_cart_button = self.wait_until(EC.element_to_be_clickable, self.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()
        return self.wait_until(EC.visibility_of_element_located, self.SUCCESS_MESSAGE)

    def go_to_cart(self):
        self.driver.find_element(*self.SHOPPING_CART_LINK).click()
        self.wait_until(EC.presence_of_element_located, (By.CSS_SELECTOR, '.cart'))

    def get_cart_items(self):
        return self.driver.find_elements(*self.CART_ITEMS)

    def remove_item_from_cart(self):
        self.driver.find_element(*self.REMOVE_CHECKBOX).click()
        self.driver.find_element(*self.UPDATE_CART_BUTTON).click()

    def get_empty_cart_message(self):
        return self.wait_until(EC.visibility_of_element_located, self.EMPTY_CART_MESSAGE)
