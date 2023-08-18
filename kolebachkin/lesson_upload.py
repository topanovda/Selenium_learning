import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/upload")

time.sleep(3)

upload_field = driver.find_element("xpath", "//input[@type='file']")
upload_field.send_keys(f"{os.getcwd()}\downloads\megadyneBladeHero.jpg")

time.sleep(3)
