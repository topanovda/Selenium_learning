import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 20, poll_frequency=1)

link = "https://stepik.org/lesson/236895/step/1"
y = "login"
x = "pass"


def test_stepik_auth(driver):
    driver.get(link)
    button = (
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(("xpath", "//a[@id='ember33']"))
        )
    ).click()
    input = driver.find_element("xpath", "//input[@id='id_login_email']").send_keys(y)
    input = driver.find_element("xpath", "//input[@id='id_login_password']").send_keys(
        x
    )
    button = (
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(("xpath", "//button[@type='submit']"))
        )
    ).click()
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element("class name", "top-tools__lesson-name")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "parametrisation test" == welcome_text
