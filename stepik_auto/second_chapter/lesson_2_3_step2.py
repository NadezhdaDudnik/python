from selenium.webdriver.chrome import webdriver


link = ""
def alert(param):
    pass

browser = webdriver.Chrome()
browser.get(link)
alert('Hello!');

alert = browser.switch_to.alert
alert.accept()
alert_text = alert.text

confirm = browser.switch_to.alert
confirm.accept()
confirm.dismiss()

prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()
prompt.dismiss()

#Переход на новую вкладку браузера
browser.switch_to.window(new_window)

#Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:

new_window = browser.window_handles[1]

#имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:

first_window = browser.window_handles[0]

# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)