import time
import math
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "normal"
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
link = "https://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    # driver = webdriver.Chrome()
    driver.get(link)

    x_element = driver.find_element("xpath", "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)
    input = driver.find_element("xpath", "//input[@id='answer']")
    input.send_keys(y)    

    option1 = driver.find_element("xpath", "(//label[@class='form-check-label'])[1]").click()
    option2 = driver.find_element("xpath", "(//label[@class='form-check-label'])[2]").click()
    button = driver.find_element("xpath", "//button[@type='submit']").click()
    # print(y)
    # time.sleep(10)
    
  
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла