# from lesson3_2_step13 import check_page
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def check_page(link):
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(
        By.CSS_SELECTOR, "input[placeholder='Input your first name']"
    )
    name.send_keys("ilya")

    surname = browser.find_element(
        By.CSS_SELECTOR, "input[placeholder='Input your last name']"
    )
    surname.send_keys("okorokov")

    email = browser.find_element(
        By.CSS_SELECTOR, "input[placeholder='Input your email']"
    )
    email.send_keys("email@ee.ee")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    return welcome_text


class TestRegistration(unittest.TestCase):

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = check_page(link)
        self.assertEqual(
            "Congratulations! You have successfully registered!", welcome_text
        )

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = check_page(link)
        self.assertEqual(
            "Congratulations! You have successfully registered!", welcome_text
        )


if __name__ == "__main__":
    unittest.main()
