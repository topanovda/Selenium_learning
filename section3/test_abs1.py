import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# chrome_options = webdriver.ChromeOptions()
# chrome_options.page_load_strategy = "normal"
# chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=chrome_options)
link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


# try:
class TestAbs(unittest.TestCase):
    def test_abs1(self):
        driver = webdriver.Chrome(service=service)
        driver.get(link1)
        self.input1 = driver.find_element(
            "xpath", "(//input[@class='form-control first'])[1]"
        )
        self.input1.send_keys("Petrov")
        self.input2 = driver.find_element(
            "xpath", "(//input[@class='form-control second'])[1]"
        )
        self.input2.send_keys("Ivan")
        self.input3 = driver.find_element(
            "xpath", "//input[@placeholder='Input your email']"
        )
        self.input3.send_keys("pwtrov@mail.ru")
        button = driver.find_element("xpath", "//button[@type='submit']").click()
        time.sleep(1)

        # находим элемент, содержащий текст
        self.welcome_text_elt = driver.find_element("tag name", "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        self.welcome_text = self.welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == self.welcome_text
        # self.assertEqual(
        #     "Congratulations! You have successfully registered!" == self.welcome_text
        # )
        driver.quit()

    def test_abs2(self):
        driver = webdriver.Chrome(service=service)
        driver.get(link2)
        self.input1 = driver.find_element(
            "xpath", "(//input[@class='form-control first'])[1]"
        )
        self.input1.send_keys("Petrov")
        self.input2 = driver.find_element(
            "xpath", "//input[@placeholder='Input your last name']"
        )
        self.input2.send_keys("Ivan")
        self.input3 = driver.find_element(
            "xpath", "//input[@placeholder='Input your email']"
        )
        self.input3.send_keys("pwtrov@mail.ru")
        button = driver.find_element("xpath", "//button[@type='submit']").click()
        time.sleep(1)

        # находим элемент, содержащий текст
        self.welcome_text_elt = driver.find_element("tag name", "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        self.welcome_text = self.welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == self.welcome_text
        # self.assertEqual(
        #     "Congratulations! You have successfully registered!" == self.welcome_text
        # )


if __name__ == "__main__":
    unittest.main()


# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     driver.quit()

# # не забываем оставить пустую строку в конце файла
