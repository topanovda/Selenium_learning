import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "normal"
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
link = "http://suninjuly.github.io/registration1.html"


try:
    # driver = webdriver.Chrome()
    driver.get(link)

    input1 = driver.find_element("xpath", "(//input[@class='form-control first'])[1]")
    input1.send_keys("Petrov")
    input2 = driver.find_element(
        "xpath", "//input[@placeholder='Input your last name']"
    )
    input2.send_keys("Ivan")
    input3 = driver.find_element("xpath", "//input[@placeholder='Input your email']")
    input3.send_keys("pwtrov@mail.ru")
    button = driver.find_element("xpath", "//button[@type='submit']").click()
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element("tag name", "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла
