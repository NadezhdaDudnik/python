from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get(link)

lakehouse_text = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price"), "$100")
    )
#assert "$100" in lakehouse_text.text

button_book = browser.find_element(By.ID, "book")
button_book.click()

x = browser.find_element(By.ID, "input_value")
x_element = int(x.text)
y = calc(x_element)

input_field = browser.find_element(By.CLASS_NAME, "form-control")
input_field.send_keys(y)

submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
submit_button.click()
