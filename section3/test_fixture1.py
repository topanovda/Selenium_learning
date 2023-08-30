from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

link = "http://selenium1py.pythonanywhere.com/"


# class TestMainPage1:
#     @classmethod
#     def setup_class(self):
#         print("\nstart browser for test suite..")
#         self.driver = webdriver.Chrome()

#     @classmethod
#     def teardown_class(self):
#         print("quit browser for test suite..")
#         self.driver.quit()

#     def test_guest_should_see_login_link(self):
#         self.driver.get(link)
#         self.driver.find_element("css selector", "#login_link")

#     def test_guest_should_see_basket_link_on_the_main_page(self):
#         self.driver.get(link)
#         self.driver.find_element("css selector", ".basket-mini .btn-group > a")


class TestMainPage2:
    def setup_method(self):
        print("start browser for test..")
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test..")
        self.driver.quit()

    def test_guest_should_see_login_link(self):
        self.driver.get(link)
        self.driver.find_element("css selector", "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.driver.get(link)
        self.driver.find_element("css selector", ".basket-mini .btn-group > a")
