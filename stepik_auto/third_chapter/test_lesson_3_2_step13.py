from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


def fill_form_registration(link):
    browser = webdriver.Chrome()
    browser.get(link)
    input_firstname = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first')
    input_firstname.send_keys("Nadya")
    input_lastname = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second')
    input_lastname.send_keys("Ailina")
    input_email = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')
    input_email.send_keys("test@test.ru")
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    # Проверяем, что смогли зарегистрироваться ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    return welcome_text


class TestRegistration(unittest.TestCase):

    def test_registration1(self):
        self.assertEqual(fill_form_registration("http://suninjuly.github.io/registration1.html"),
                         "Congratulations! You have successfully registered!", "Registration is failed")

    def test_registration2(self):
        self.assertEqual(fill_form_registration("http://suninjuly.github.io/registration2.html"),
                         "Congratulations! You have successfully registered!", "Registration is failed")


if __name__ == "__main__":
    unittest.main()