from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
import math


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(5)
wait = WebDriverWait(browser, 10)
button = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "button.btn-add-to-basket[type='Submit']")
    )
)
button.click()

book_price = browser.find_element(By.CSS_SELECTOR, "p.price_color")


message1 = browser.find_element(By.CSS_SELECTOR, "div.alertinner ")
message2 = message1.find_element(By.CSS_SELECTOR, "strong")

total_message = "The shellcoder's handbook  был добавлен в вашу корзину."
assert message2.text + message1.text == total_message


def solve_quiz_and_get_code(self):
    alert = self.browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")
