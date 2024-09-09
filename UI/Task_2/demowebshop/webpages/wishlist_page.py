from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from UI.Task_2.demowebshop.webpages.base_page import BasePage


class WishlistPage(BasePage):
    WISHLIST_CONTENT = (By.CSS_SELECTOR, '.wishlist-content')
    PRODUCT_SUBTOTAL = (By.CSS_SELECTOR, ".product-subtotal")

    def navigate_to_wishlist(self):
        self.driver.find_element(By.LINK_TEXT, 'Wishlist').click()

    def wait_for_wishlist_content(self):
        self.wait_until(EC.presence_of_element_located, self.WISHLIST_CONTENT)

    def get_product_price(self):
        return self.driver.find_element(*self.PRODUCT_SUBTOTAL).text
