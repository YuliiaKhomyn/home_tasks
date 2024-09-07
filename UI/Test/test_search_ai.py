from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from UI.Test.conftest import URL
from UI.Test.conftest import driver


def test_search_ai(driver):
    driver.get(URL)

    search_icon = driver.find_element(By.CSS_SELECTOR, ".search-icon")
    search_icon.click()

    search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#new_form_search')))
    search.send_keys("AI")
    find_button = driver.find_element(By.CSS_SELECTOR, ".custom-button")
    find_button.click()

    result_items = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.search-results__item')))

    assert len(result_items) > 0
