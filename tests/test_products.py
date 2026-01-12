from config.config import Config
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_products_page_loaded(page):
    login = LoginPage(page)
    login.navigate(Config.BASE_URL)
    login.login(Config.VALID_USER, Config.VALID_PASSWORD)

    products = ProductsPage(page)
    assert products.get_title() == "Products"
