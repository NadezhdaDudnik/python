from selenium import webdriver
import time

driver = webdriver.Chrome('/usr/local/bin/chromedriver');
driver.get('http://itcareer.pythonanywhere.com/')

web_form = driver.find_elements_by_class_name('form-group');

name_field = driver.find_element_by_id('name')
name_field.send_keys('Nadin')
time.sleep(3)

surname_field = driver.find_element_by_id('surname')
surname_field.send_keys('seo')
time.sleep(3)

email_field = driver.find_element_by_id('email')
email_field.send_keys('seo@mail.ru')
time.sleep(3)

password_field = driver.find_element_by_id('password')
password_field.send_keys('37487594')
time.sleep(3)

submit_button = driver.find_element_by_tag_name('button')
submit_button.click()

success_message = driver.find_element_by_tag_name('strong')
print(success_message.text)

message_path = ''
success_message_2 = driver.find_elements_by_xpath(message_path)

if 'Success' in success_message_2.text:
    print('Test_success_message - Passed')
else:
    print('Test_success_message - failed')

driver.close