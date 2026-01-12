class CartPage:

    def __init__(self, page):
        self.page = page
        self.checkout_btn = "#checkout"

    def click_checkout(self):
        self.page.wait_for_selector(self.checkout_btn)
        self.page.click(self.checkout_btn)
