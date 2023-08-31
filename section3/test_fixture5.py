import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="class")
def driver():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser..")
    driver.quit()


class TestMainPage1:
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, driver):
        print("start test1")
        driver.get(link)
        driver.find_element("css selector", "#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, driver):
        print("start test2")
        driver.get(link)
        driver.find_element("css selector", ".basket-mini .btn-group > a")
        print("finish test2")
