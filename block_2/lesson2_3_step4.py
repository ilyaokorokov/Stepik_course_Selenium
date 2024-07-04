from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button_submit = browser.find_element(By.CSS_SELECTOR, "button[type='Submit']")
button_submit.click()

confirm = browser.switch_to.alert
confirm.accept()

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)

answer = browser.find_element(By.CSS_SELECTOR, "#answer")
answer.send_keys(y)

button_submit1 = browser.find_element(By.CSS_SELECTOR, "button[type='Submit']")
button_submit1.click()

time.sleep(10)
browser.quit()
