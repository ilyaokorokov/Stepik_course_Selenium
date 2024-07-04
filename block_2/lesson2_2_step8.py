from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

first_name = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
first_name.send_keys("ilya")

last_name = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
last_name.send_keys("okorokov")

email = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
email.send_keys("email")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file.txt"
file_path = os.path.join(current_dir, file_name)

element = browser.find_element(By.CSS_SELECTOR, "input#file")
element.send_keys(file_path)

button_submit = browser.find_element(By.CSS_SELECTOR, "button[type='Submit']")
button_submit.click()

time.sleep(10)
browser.quit()
