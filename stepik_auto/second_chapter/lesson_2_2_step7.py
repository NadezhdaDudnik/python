import os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

firstname = browser.find_element(By.NAME, "firstname")
firstname.send_keys("Nadya")

lastname = browser.find_element(By.NAME, "lastname")
lastname.send_keys("Ilina")

email = browser.find_element(By.NAME, "email")
email.send_keys("user@mail.ru")

# получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))
# добавляем к этому пути имя файла - должны лежать в одной папке
file_path = os.path.join(current_dir, 'file.txt')

# create test.txt file
#with open("test.txt", "w") as file:
    #content = file.write("automationbypython")

element = browser.find_element(By.NAME, "file")
element.send_keys(file_path)

submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
submit_button.click()