from UI.Task_2.demowebshop.conftest import driver
from UI.Task_2.demowebshop.webpages.cart_page import CartPage
from UI.Task_2.demowebshop.webpages.product_page import ProductPage


def test_add_item_to_cart(driver):
    product_page = ProductPage(driver)
    product_page.go_to_product_page('50s-rockabilly-polka-dot-top-jr-plus-size')

    cart_page = CartPage(driver)

    success_message = cart_page.add_item_to_cart()
    assert "The product has been added to your shopping cart" in success_message.text

    cart_page.go_to_cart()
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) > 0, "No items found in the shopping cart."


def test_remove_item_from_cart(driver):
    product_page = ProductPage(driver)
    product_page.go_to_product_page('50s-rockabilly-polka-dot-top-jr-plus-size')

    cart_page = CartPage(driver)
    cart_page.add_item_to_cart()
    cart_page.go_to_cart()
    cart_page.remove_item_from_cart()

    cart_items = cart_page.get_cart_items()
    assert len(cart_items) == 0, "The item was not removed from the shopping cart."

    empty_cart_message = cart_page.get_empty_cart_message()
    assert "Your Shopping Cart is empty!" in empty_cart_message.text
