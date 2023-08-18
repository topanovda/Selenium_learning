import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.rambler.ru/")

driver.find_element("xpath", "//a[.='Войти в почту']").click()

time.sleep(5)   