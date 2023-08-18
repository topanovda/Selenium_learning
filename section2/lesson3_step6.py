import time
import math
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

link = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.get(link)
    button = driver.find_element("xpath", "//button[@type='submit']").click()
    # переходм в новое открывшиеся окно
    driver.switch_to.window(driver.window_handles[1])
    # находим число и вычисляем его
    x = (driver.find_element("xpath", "//span[@id='input_value']")).text
    y = calc(x)
    # подставляем в поле
    input = driver.find_element("xpath", "//input[@id='answer']").send_keys(y)
    # сликаем кнопку Submit
    button = driver.find_element("xpath", "//button[@type='submit']").click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла
