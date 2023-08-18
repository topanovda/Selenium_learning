import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


try:
    # driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/huge_form.html")
    elements = driver.find_elements("xpath", "//input[@type='text']")
    for element in elements:
        element.send_keys("Мой ответ")

    button = driver.find_element("xpath", "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла