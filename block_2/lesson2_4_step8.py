from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

wait = WebDriverWait(browser, 10)
element = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

book = browser.find_element(By.CSS_SELECTOR, "#book")
book.click()

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)

answer = browser.find_element(By.CSS_SELECTOR, "#answer")
answer.send_keys(y)

button_submit1 = browser.find_element(By.CSS_SELECTOR, "button[type='Submit']")
button_submit1.click()

time.sleep(10)
browser.quit()
