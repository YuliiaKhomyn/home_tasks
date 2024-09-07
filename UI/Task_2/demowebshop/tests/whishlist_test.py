from UI.Task_2.demowebshop.conftest import driver
from UI.Task_2.demowebshop.webpages.product_page import ProductPage
from UI.Task_2.demowebshop.webpages.wishlist_page import WishlistPage


def test_add_item_to_wishlist(driver):
    product_page = ProductPage(driver)
    product_page.go_to_product_page('50s-rockabilly-polka-dot-top-jr-plus-size')
    product_page.wait_for_item_box()
    product_page.add_to_wishlist()

    success_message = product_page.wait_for_success_message()
    assert "The product has been added to your wishlist" in success_message.text

    wishlist_page = WishlistPage(driver)
    wishlist_page.navigate_to_wishlist()
    wishlist_page.wait_for_wishlist_content()

    product_price = wishlist_page.get_product_price()
    assert product_price == '11.00'
