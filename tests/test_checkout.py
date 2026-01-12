from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config.config import Config

def test_complete_checkout_flow(page):

    # Login
    login = LoginPage(page)
    login.navigate(Config.BASE_URL)
    login.login(Config.VALID_USER, Config.VALID_PASSWORD)

    # Products
    products = ProductsPage(page)
    assert products.get_title() == "Products"

    products.add_product_to_cart("Sauce Labs Bolt T-Shirt")
    products.go_to_cart()

    # Cart
    cart = CartPage(page)
    cart.click_checkout()

    # Checkout
    checkout = CheckoutPage(page)
    checkout.enter_checkout_details("Vineet", "Raj", "560001")
    checkout.finish_order()

    # Validation
    assert checkout.get_success_message() == "Thank you for your order!"
