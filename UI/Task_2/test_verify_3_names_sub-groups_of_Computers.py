from selenium.webdriver.common.by import By
from configuration import driver


def test_computers_group_subgroups(driver):
    driver.get('https://demowebshop.tricentis.com/')
    driver.find_element(By.LINK_TEXT, 'Computers').click()
    sub_category_grid = driver.find_element(By.CSS_SELECTOR, '.block-category-navigation')
    active_sublist = sub_category_grid.find_element(By.CSS_SELECTOR, '.active > .sublist')
    actual_titles = [title.text for title in active_sublist.find_elements(By.CSS_SELECTOR, 'a')]
    expected_subgroups = ['Desktops', 'Notebooks', 'Accessories']

    assert len(actual_titles) == len(expected_subgroups)
    assert set(actual_titles) == set(expected_subgroups)
