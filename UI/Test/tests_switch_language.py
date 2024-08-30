from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from configuration import URL
from configuration import driver


def test_open_epam_and_check_element(driver):
    driver.get(URL)

    header_controls = driver.find_element(By.CSS_SELECTOR, '.header__controls')
    header_controls.find_element(By.CSS_SELECTOR, '.location-selector__button').click()
    locations = driver.find_elements(By.CSS_SELECTOR, '.location-selector__item')

    for location in locations:
        if location.find_elements(By.CSS_SELECTOR, '[lang="uk"]'):
            clickable_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(location))
            clickable_element.click()
            break

    actual_lang = (WebDriverWait(driver, 10)
                   .until(EC.presence_of_element_located((By.CSS_SELECTOR, '.no-touchevents'))).get_attribute('lang'))

    assert actual_lang == 'uk-UA', f"Expected 'uk-UA', but got '{actual_lang}'"

