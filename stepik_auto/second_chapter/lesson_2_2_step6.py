from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://SunInJuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input_field = browser.find_element(By.CSS_SELECTOR, '[type="text"]')
    input_field.send_keys(y)

    browser.execute_script("window.scrollBy(0, 100);")

    checkbox = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    radiobutton.click()

    submit_button = browser.find_element(By.TAG_NAME, 'button')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()



