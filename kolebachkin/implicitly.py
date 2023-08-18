from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--ignore-sertificate-errors")
# говорим WebDriver искать каждый элемент в течение 5 секунд
driver.implicitly_wait(10)

driver.get("https://demoqa.com/dynamic-properties")
VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']")

driver.find_element(*VISIBLE_AFTER_BUTTON).click()
