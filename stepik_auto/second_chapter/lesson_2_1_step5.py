from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    print(y)
    insert_value = browser.find_element(By.CSS_SELECTOR, '[type = "text"]')
    insert_value.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    checkbox.click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    radiobutton.click()
    button_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button_submit.click();

finally:
    time.sleep(10)
    browser.quit()
