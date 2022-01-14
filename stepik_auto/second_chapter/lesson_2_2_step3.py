from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

#link = "http://suninjuly.github.io/selects1.html"
link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element(By.ID, "num1")

    num2 = browser.find_element(By.ID, "num2")
    n1 = int(num1.text)
    print("n1 = ", n1)

    n2 = int(num2.text)
    print("n2 = ", n2)

    summa = n1 + n2
    print("summa =", summa)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(summa))

    button_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()







