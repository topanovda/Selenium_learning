import time
import math
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "normal"
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
link = "http://suninjuly.github.io/selects2.html"

# def calc(x):
#     return sum(str(str(int(a)+int(b))))

try:
    
    driver.get(link)  

    a = int(driver.find_element("id", "num1").text)
    b = int(driver.find_element("id", "num2").text)
    c = (a + b)
    d = str(c)

    select = Select(driver.find_element("tag name", "select"))
    select.select_by_value(d) # ищем элемент с текстом "Python"
    button = driver.find_element("xpath", "//button[@type='submit']").click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла