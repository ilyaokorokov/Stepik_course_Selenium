from base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(
            By.CSS_SELECTOR, "button.btn-add-to-basket[type='submit']"
        )
        button.click()
        
    # def get_product_name(self):
    #     return self.browser.find_element(By.CSS_SELECTOR, "div.alertinner strong").text

    # def get_product_price(self):
    #     return self.browser.find_element(By.CSS_SELECTOR, "p.price_color").text

    # def should_be_success_message(self, product_name):
    #     success_message = self.browser.find_element(
    #         By.CSS_SELECTOR, "div.alertinner "
    #     ).text
    #     assert (
    #         product_name in success_message
    #     ), "Success message does not contain the product name"

    # def should_be_correct_basket_total(self, product_price):
    #     basket_total = self.browser.find_element(
    #         By.CSS_SELECTOR, "div.alertinner p.price_color"
    #     ).text
    #     assert (
    #         product_price == basket_total
    #     ), "Basket total does not match product price"
