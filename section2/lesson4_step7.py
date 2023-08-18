import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# говорим WebDriver искать каждый элемент в течение 5 секунд
driver.implicitly_wait(5)

link = "http://suninjuly.github.io/wait2.html"


try:
    driver.get(link)
    button = (
        WebDriverWait(driver, 5)
        .until(EC.element_to_be_clickable(("xpath", "//button[@id='verify']")))
        .click()
    )
    # button = driver.find_element("xpath", "//button[@id='verify']").click()
    message = driver.find_element("xpath", "//div[@id='verify_message']")

    assert "successful" in message.text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла
