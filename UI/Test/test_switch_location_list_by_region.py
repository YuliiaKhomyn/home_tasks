from configuration import driver
from configuration import URL
from selenium.webdriver.common.by import By



def test_exist_location_list_by_region(driver):
    driver.get(URL)

    our_Locations_tab = driver.find_element(By.CSS_SELECTOR, ".tabs-23__ul-wrapper")
    our_Locations = our_Locations_tab.find_elements(By.CSS_SELECTOR, ".tabs-23__link.js-tabs-link")

    actual_our_Locations_list = []

    for location in our_Locations:
        actual_our_Locations_list.append(location.text)

    expected_our_Locations_list = ['AMERICAS', 'EMEA', 'APAC']

    for l in expected_our_Locations_list:
        assert l in actual_our_Locations_list, f"Expected {l} to be in the list."


def test_switch_location_list_by_region(driver):
    driver.get(URL)

    our_Locations_tab = driver.find_element(By.CSS_SELECTOR, ".tabs-23__ul-wrapper")
    our_Locations = our_Locations_tab.find_elements(By.CSS_SELECTOR, ".tabs-23__link.js-tabs-link")

    for location in our_Locations:
        driver.execute_script("arguments[0].click();", location)

        classes = location.get_attribute("class")
        assert "active" in classes, f"{location.text} should be active, but it isn't."

        for other_location in our_Locations:
            if other_location != location:
                other_classes = other_location.get_attribute("class")
                assert "active" not in other_classes, f"{other_location.text} should not be active, but it is."