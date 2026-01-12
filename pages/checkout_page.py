class CheckoutPage:

    def __init__(self, page):
        self.page = page

        self.first_name = "#first-name"
        self.last_name = "#last-name"
        self.zip_code = "#postal-code"
        self.continue_btn = "#continue"
        self.finish_btn = "#finish"
        self.success_msg = ".complete-header"

    def enter_checkout_details(self, fname, lname, zip_code):
        self.page.fill(self.first_name, fname)
        self.page.fill(self.last_name, lname)
        self.page.fill(self.zip_code, zip_code)
        self.page.click(self.continue_btn)

    def finish_order(self):
        self.page.click(self.finish_btn)

    def get_success_message(self):
        return self.page.text_content(self.success_msg)
