from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element("name", "first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element("name", "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element("name", "firstname")
    input3.send_keys("Smolensk")
    input4 = browser.find_element("id", "country")
    input4.send_keys("Russia")
    button = browser.find_element("css selector", "#submit_button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла``