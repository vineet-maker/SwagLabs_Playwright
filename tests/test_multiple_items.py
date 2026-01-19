from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from config.config import Config

def test_add_multiple_items(page):
    login = LoginPage(page)
    products = ProductsPage(page)

    login.navigate(Config.BASE_URL)
    login.login(Config.VALID_USER, Config.VALID_PASSWORD)

    products.add_product_to_cart("Sauce Labs Backpack")
    products.add_product_to_cart("Sauce Labs Bike Light")
    products.add_product_to_cart("Sauce Labs Bolt T-Shirt")

    products.go_to_cart()

    assert page.locator(".cart_item").count() == 3
