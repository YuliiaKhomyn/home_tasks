from configuration import URL
from configuration import driver
from selenium.webdriver.common.by import By


def test_verify_policies_list(driver):
    driver.get(URL)

    policies_box = driver.find_element(By.CSS_SELECTOR, ".policies-links-wrapper")
    policies = policies_box.find_elements(By.CSS_SELECTOR, ".fat-links")

    actual = []

    for policy in policies:
        actual.append(policy.text)

    expected = ['INVESTORS', 'COOKIE POLICY', 'OPEN SOURCE', 'APPLICANT PRIVACY NOTICE', 'PRIVACY POLICY',
                'WEB ACCESSIBILITY']

    for p in expected:
        assert p in actual, f"Expected {p} to be in the list."


