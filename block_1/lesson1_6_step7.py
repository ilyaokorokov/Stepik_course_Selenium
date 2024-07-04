from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/huge_form.html"


browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")
for element in input1:
    element.send_keys("Ivan")

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(10)
browser.quit()
