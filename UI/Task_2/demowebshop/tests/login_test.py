from UI.Task_2.demowebshop.conftest import driver
from UI.Task_2.demowebshop.webpages.home_page import HomePage
from UI.Task_2.demowebshop.webpages.login_page import LoginPage


def test_login_user(driver):
    home_page = HomePage(driver)
    home_page.go_to_home_page()

    login_page = LoginPage(driver)
    login_page.click_login_link()
    login_page.enter_email('testuser11e0e9fa912c4bb6866c80a29563eaa8@example.com')
    login_page.enter_password('Password123')
    login_page.click_login()

    welcome_message = login_page.get_welcome_message()
    assert "Log out" in welcome_message.text
