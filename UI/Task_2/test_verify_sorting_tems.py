import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from configuration import driver

@pytest.fixture(params=[
    ("Position", lambda x: x),
    ("Name: A to Z", lambda x: x),
    ("Price: Low to High", sorted),
    ("Price: High to Low", lambda x: sorted(x, reverse=True)),
    ("Created on", lambda x: x)
])
def sort_option(request):
    return request.param


def get_sorted_prices(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.item-box'))
    )
    prices = driver.find_elements(By.CSS_SELECTOR, '.prices .price')
    prices = [float(price.text.replace('$', '').replace(',', '')) for price in prices]
    return prices


def test_sorting_products(driver, sort_option):
    driver.get('https://demowebshop.tricentis.com/accessories')

    sort_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'products-orderby'))
    )
    sort_dropdown.send_keys(sort_option[0])
    prices = get_sorted_prices(driver)

    assert prices == sort_option[1](prices), f"Products are not sorted by {sort_option[0]}"