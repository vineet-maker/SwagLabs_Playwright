from pages.login_page import LoginPage
from config.config import BASE_URL, VALID_USER, VALID_PASSWORD, INVALID_USER

def test_valid_login(page):
    login_page = LoginPage(page)

    login_page.navigate(BASE_URL)
    login_page.login(VALID_USER, VALID_PASSWORD)

    assert "inventory" in page.url


def test_invalid_login(page):
    login_page = LoginPage(page)

    login_page.navigate(BASE_URL)
    login_page.login(INVALID_USER, VALID_PASSWORD)

    error = login_page.get_error_message()
    assert "locked out" in error.lower()
