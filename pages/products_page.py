class ProductsPage:

    def __init__(self, page):
        self.page = page
        self.title = ".title"
        self.cart_icon = "[data-test='shopping-cart-link']"

    def get_title(self):
        return self.page.text_content(self.title)

    def add_product_to_cart(self, product_name):
        """
        product_name example:
        'Sauce Labs Bolt T-Shirt'
        """
        add_btn = (
            f"//div[text()='{product_name}']"
            "/ancestor::div[@class='inventory_item']"
            "//button"
        )
        self.page.click(add_btn)

    def go_to_cart(self):
        self.page.click(self.cart_icon)
