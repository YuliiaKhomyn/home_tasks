import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from configuration import driver

@pytest.fixture(params=[4, 8, 12])
def items_per_page_option(request):
    return request.param


def test_items_per_page(driver, items_per_page_option):
    driver.get('https://demowebshop.tricentis.com/apparel-shoes')

    items_per_page_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'products-pagesize'))
    )
    items_per_page_dropdown.send_keys(str(items_per_page_option))

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.item-box'))
    )
    items = driver.find_elements(By.CSS_SELECTOR, '.item-box')

    number_of_items = len(items)

    assert number_of_items == items_per_page_option, (
        f"Expected {items_per_page_option} items, but found {number_of_items}.")