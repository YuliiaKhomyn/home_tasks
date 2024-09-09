from UI.Task_2.demowebshop.conftest import driver
from UI.Task_2.demowebshop.webpages.cart_page import CartPage
from UI.Task_2.demowebshop.webpages.checkout_page import CheckoutPage
from UI.Task_2.demowebshop.webpages.login_page import LoginPage
from UI.Task_2.demowebshop.webpages.product_page import ProductPage


def test_checkout_item(driver):
    login_page = LoginPage(driver)
    login_page.go_to_home_page()
    login_page.click_login_link()
    login_page.enter_email('testuser11e0e9fa912c4bb6866c80a29563eaa8@example.com')
    login_page.enter_password('Password123')
    login_page.click_login()
    login_page.get_welcome_message()

    product_page = ProductPage(driver)
    product_page.go_to_product_page('50s-rockabilly-polka-dot-top-jr-plus-size')

    cart_page = CartPage(driver)
    cart_page.add_item_to_cart()
    cart_page.go_to_cart()

    checkout_page = CheckoutPage(driver)
    checkout_page.agree_terms_of_service()
    checkout_page.proceed_to_checkout()
    checkout_page.click_new_address_next_step()
    checkout_page.click_new_address_checkout_step()
    checkout_page.click_shipping_method_next_step()
    checkout_page.click_payment_method_next_step()
    checkout_page.click_payment_info_next_step()
    checkout_page.click_confirm_order_next_step()

    order_confirmation_message = checkout_page.get_order_confirmation_message()
    assert "Your order has been successfully processed" in order_confirmation_message.text
