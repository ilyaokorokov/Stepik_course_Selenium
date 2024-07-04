from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def test_language_add_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    wait = WebDriverWait(browser, 10)
    button = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "button.btn-add-to-basket[type='Submit']")
        )
    )

    assert button.text in [
        "Añadir al carrito",
        "Ajouter au panier",
        "Добавить в корзину",
    ], f"Unexpected button text (try es, ru or fr): {button.text}"
