from selenium import webdriver
from selenium.webdriver.common.by import By
import math

import time

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
button.click()

confirm = browser.switch_to.alert
confirm.accept()

x = browser.find_element(By.ID, "input_value")
x_element = int(x.text)
y = calc(x_element)

input_field = browser.find_element(By.CLASS_NAME, "form-control")
input_field.send_keys(y)

submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
submit_button.click()