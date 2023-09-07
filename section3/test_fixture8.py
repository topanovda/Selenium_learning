import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def driver():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser..")
    driver.quit()


@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("preparing some critical data for every test")


class TestMainPage1:
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, driver):
        # не передаём как параметр фикстуру prepare_data, но она все равно выполняется
        driver.get(link)
        driver.find_element("css selector", "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, driver):
        driver.get(link)
        driver.find_element("css selector", ".basket-mini .btn-group > a")
