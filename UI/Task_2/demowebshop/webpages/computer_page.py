from selenium.webdriver.common.by import By

from UI.Task_2.demowebshop.webpages.base_page import BasePage


class ComputerPage(BasePage):
    SUB_CATEGORY_GRID = (By.CSS_SELECTOR, '.block-category-navigation')
    ACTIVE_SUBLIST = (By.CSS_SELECTOR, '.active > .sublist')
    TAG_A = (By.CSS_SELECTOR, 'a')

    def get_subgroup_titles(self):
        sub_category_grid = self.driver.find_element(*self.SUB_CATEGORY_GRID)
        active_sublist = sub_category_grid.find_element(*self.ACTIVE_SUBLIST)
        titles = [element.text for element in active_sublist.find_elements(*self.TAG_A)]
        return titles
