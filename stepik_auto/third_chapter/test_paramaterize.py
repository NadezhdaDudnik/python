import pytest
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\n quit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ["236895", "236896", "236897", "236898",
                             "236899", "236903", "236904", "236905"])
def test_get_link(browser, link):
    answer = str(math.log(int(time.time())))
    mainlink = f"https://stepik.org/lesson/{link}/step/1"
    browser.get(mainlink)
    browser.implicitly_wait(100)
    input_text = browser.find_element(By.CSS_SELECTOR, '.ember-text-area')

    input_text.send_keys(answer)
    browser.implicitly_wait(100)
    button_send = browser.find_element(By.CSS_SELECTOR, '[class="submit-submission"]')
    button_send.click()
    correct_text = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint')
    correct = correct_text.text

    assert "Correct!" == correct, "Wrong answer"
