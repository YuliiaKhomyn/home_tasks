import pytest

from UI.Task_2.demowebshop.conftest import driver
from UI.Task_2.demowebshop.webpages.category_page import CategoryPage


@pytest.mark.parametrize("items_per_page_option", [4, 8, 12])
def test_items_per_page(driver, items_per_page_option):
    category_page = CategoryPage(driver)
    category_page.go_to_category_page('apparel-shoes')
    category_page.select_items_per_page(items_per_page_option)
    number_of_items = category_page.get_number_of_items_displayed()
    assert number_of_items == items_per_page_option, f"Expected {items_per_page_option} items, but found {number_of_items}."


@pytest.mark.parametrize("sort_option, sort_function", [
    ("Position", lambda x: x),
    ("Name: A to Z", lambda x: x),
    ("Price: Low to High", sorted),
    ("Price: High to Low", lambda x: sorted(x, reverse=True)),
    ("Created on", lambda x: x)
])
def test_sorting_products(driver, sort_option, sort_function):
    category_page = CategoryPage(driver)
    category_page.go_to_category_page('accessories')
    category_page.select_sort_option(sort_option)
    prices = category_page.get_sorted_prices()

    assert prices == sort_function(prices), f"Products are not sorted by {sort_option}"
