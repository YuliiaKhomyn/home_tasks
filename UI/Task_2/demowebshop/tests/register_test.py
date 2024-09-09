import uuid

from UI.Task_2.demowebshop.webpages.register_page import RegisterPage


def test_register_user(driver):
    register_page = RegisterPage(driver)
    register_page.go_to_home_page()
    register_page.click_register_link()
    register_page.enter_male_gender()
    register_page.enter_first_name('Test')
    register_page.enter_last_name('User')
    register_page.enter_email(f"testuser{uuid.uuid4().hex}@example.com")
    register_page.enter_password('Password123')
    register_page.enter_confirm_password('Password123')
    register_page.click_confirm_register()

    success_message = register_page.get_success_message()
    assert "Your registration completed" in success_message.text
