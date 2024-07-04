from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

answer = browser.find_element(By.CSS_SELECTOR, "#answer")
answer.send_keys(y)

i_am_the_robot = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
i_am_the_robot.click()

robots_rule = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
robots_rule.click()

button_submit = browser.find_element(By.CSS_SELECTOR, "button[type='Submit']")
button_submit.click()

time.sleep(10)
browser.quit()
