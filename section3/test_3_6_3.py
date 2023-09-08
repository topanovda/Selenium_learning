import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser..")
    driver.quit()

    # @pytest.mark.parametrize("language", ["ru", "en-gb"])
    # def test_guest_should_see_login_link(driver, language):
    #     link = f"http://selenium1py.pythonanywhere.com/{language}/"
    #     driver.get(link)
    #     driver.find_element("css selector", "#login_link")


@pytest.mark.parametrize("language", ["ru", "en-gb"])
class TestLogin:
    def test_guest_should_see_login_link(self, driver, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        driver.get(link)
        driver.find_element("css selector", "#login_link")
        # этот тест запустится 2 раза

    def test_guest_should_see_navbar_element(self, driver, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        driver.get(link)
        driver.find_element("css selector", "#login_link")
        # этот тест тоже запустится дважды
