import pytest
from product_page import ProductPage
import time

# http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear
@pytest.mark.parametrize(
    "link",
    [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    ],
)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()

    # product_name = page.get_product_name()
    # product_price = page.get_product_price()

    # page.should_be_success_message(product_name)
    # page.should_be_correct_basket_total(product_price)
    time.sleep(10)
