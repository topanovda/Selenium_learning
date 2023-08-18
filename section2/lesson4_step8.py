import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "normal"
chrome_options.add_argument("--window-size=1920,1080")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 20, poll_frequency=1)
# говорим WebDriver искать каждый элемент в течение 5 секунд
# driver.implicitly_wait(5)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"


try:
    driver.get(link)
    # задаем значение цены бронирования
    PRICE_BOOK = ("xpath", "//h5[@id='price']")
    # задаем кнопку брнирования
    BUTTON_BOOK = ("xpath", "//button[@id='book']")
    # ловим необходимую цену бронирования
    wait.until(EC.text_to_be_present_in_element(PRICE_BOOK, "$100"))
    button = driver.find_element(*BUTTON_BOOK).click()
    # получаем число для формулы
    x = (driver.find_element("xpath", "//span[@id='input_value']")).text
    y = calc(x)
    # подставляем в поле
    input = driver.find_element("xpath", "//input[@id='answer']").send_keys(y)
    # находим кнопку Submit
    button = driver.find_element("xpath", "//button[@type='submit']")
    # Пролистываем страницу вниз, чтобы кнопка была видна
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    # сликаем кнопку Submit
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла
