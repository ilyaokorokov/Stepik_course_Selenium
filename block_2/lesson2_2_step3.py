from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
num2 = browser.find_element(By.CSS_SELECTOR, "#num2").text

result = int(num1) + int(num2)

# menu_select = Select(browser.find_element(By.TAG_NAME, "select"))
# menu_select.select_by_value(str(result))

menu_select = browser.find_element(By.CSS_SELECTOR, "#dropdown")
menu_select.click()

result1 = str(result)

values = menu_select.find_elements(By.CSS_SELECTOR, "option")
for element in values:
    if element.text == result1:
        element.click()
        break

button_submit = browser.find_element(By.CSS_SELECTOR, "button[type='Submit']")
button_submit.click()

time.sleep(10)
browser.quit()
