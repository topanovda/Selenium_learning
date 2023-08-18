import time
import math
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--window-size=1920,1080")
# service = Service(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=chrome_options)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_link_text"
text_link = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # link = browser.find_element_by_partial_link_text(text_link).click

    # driver.get(link)
    # print(math.ceil(math.pow(math.pi, math.e)*10000))
    print(text_link)
    link = browser.find_element("By.LINK_TEXT", '224592')
    link.click()
    time.sleep(2)
    input1 = browser.find_element("name", "first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element("name", "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element("name", "firstname")
    input3.send_keys("Smolensk")
    input4 = browser.find_element("id", "country")
    input4.send_keys("Russia")
    button = browser.find_element("css selector", "button[type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла``