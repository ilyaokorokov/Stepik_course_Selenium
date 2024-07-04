from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
name = browser.find_element(
    By.CSS_SELECTOR, "input[placeholder='Input your first name']"
)
name.send_keys("ilya")

surname = browser.find_element(
    By.CSS_SELECTOR, "input[placeholder='Input your last name']"
)
surname.send_keys("okorokov")

email = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
email.send_keys("email@ee.ee")
# Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(1)

welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
welcome_text = welcome_text_elt.text

assert "Congratulations! You have successfully registered!" == welcome_text

time.sleep(10)
browser.quit()
