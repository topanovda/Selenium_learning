import time
import math
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# chrome_options = webdriver.ChromeOptions()
# chrome_options.page_load_strategy = "normal"
# chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

link = "http://suninjuly.github.io/execute_script.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver.get(link)
    x = (driver.find_element("xpath", "//span[@id='input_value']")).text
    y = calc(x)
    input = driver.find_element("xpath", "//input[@id='answer']").send_keys(y) 
    button = driver.find_element("tag name", "button")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    option1 = driver.find_element("id", "robotCheckbox").click()
    option2 = driver.find_element("id", "robotsRule").click()
    button = driver.find_element("xpath", "//button[@type='submit']").click()
    
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла