from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from UI.Task_2.demowebshop.webpages.base_page import BasePage


class CategoryPage(BasePage):
    PRODUCTS_PAGESIZE_DROPDOWN = (By.ID, 'products-pagesize')
    ITEM_BOX = (By.CSS_SELECTOR, '.item-box')
    SORT_DROPDOWN = (By.ID, 'products-orderby')
    item_boxes = (By.CSS_SELECTOR, '.item-box')
    price_selector = (By.CSS_SELECTOR, '.prices .price')

    def select_sort_option(self, option_text):
        sort_dropdown = self.wait_until(EC.element_to_be_clickable, self.SORT_DROPDOWN)
        sort_dropdown.send_keys(option_text)

    def get_sorted_prices(self):
        self.wait_until(EC.presence_of_all_elements_located, self.item_boxes)
        prices = self.driver.find_elements(*self.price_selector)
        prices = [float(price.text.replace('$', '').replace(',', '')) for price in prices]
        return prices

    def go_to_category_page(self, category):
        self.driver.get(f'{self.URL}/{category}')

    def select_items_per_page(self, option):
        items_per_page_dropdown = self.wait_until(EC.element_to_be_clickable, self.PRODUCTS_PAGESIZE_DROPDOWN)
        items_per_page_dropdown.send_keys(str(option))
        WebDriverWait(self.driver, 10).until(
            lambda driver: len(driver.find_elements(*self.ITEM_BOX)) == option
        )

    def get_number_of_items_displayed(self):
        return len(self.driver.find_elements(*self.ITEM_BOX))
