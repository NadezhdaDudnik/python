from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time
import string

try:
    #Создаем строку из букв англ.алфавита в нижнем регистре
    letters = string.ascii_lowercase

    # В цикл добавляем генерацию случайного набора символов(диапазон произвольный)
    random_word = ''.join(random.choice(letters) for _ in range(8))

    browser = webdriver.Chrome();
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.CSS_SELECTOR, '[type = "text"]')
    for element in elements:
        element.send_keys(random_word)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
