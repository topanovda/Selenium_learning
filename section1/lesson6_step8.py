import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "normal"
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


try:
    # driver = webdriver.Chrome()
    driver.get(" http://suninjuly.github.io/find_xpath_form")

    input1 = driver.find_element("name", "first_name")
    input1.send_keys("Ivan")
    input2 = driver.find_element("name", "last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element("name", "firstname")
    input3.send_keys("Smolensk")
    input4 = driver.find_element("id", "country")
    input4.send_keys("Russia")
    button = driver.find_element("xpath", "//button[@type='submit']").click()
      
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла