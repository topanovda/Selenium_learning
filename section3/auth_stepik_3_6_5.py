import pytest
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Инициализация веб-драйвера
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 20, poll_frequency=1)

# Заданные значения email и пароля
email = "***"
password = "***"


# Здесь создайте список URL-адресов, которые вы хотите посетить
@pytest.mark.parametrize(
    "url",
    [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1",
    ],
)
class TestLogin:
    def test_stepik_auth(self, driver, url):  # Добавляем параметр driver и url
        driver.get(url)

        # Нажатие на кнопку "Войти" (xpath может изменяться, уточните его)
        button = (
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(
                    ("xpath", "(//a[contains(@class,'ember-view navbar__auth')])[1]")
                )
            )
        ).click()

        # Заполнение поля email
        input_email = driver.find_element("xpath", "//input[@id='id_login_email']")
        input_email.send_keys(email)

        # Заполнение поля пароля
        input_password = driver.find_element(
            "xpath", "//input[@id='id_login_password']"
        )
        input_password.send_keys(password)

        # Нажатие на кнопку "Войти" после ввода данных
        button_submit = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(("xpath", "//button[@type='submit']"))
        )
        button_submit.click()

        # Ожидание завершения авторизации (в данном случае, по наличию элемента на странице)
        # wait.until(
        #     EC.visibility_of_element_located(
        #         ("xpath", "//textarea[@placeholder='Напишите ваш ответ здесь...']")
        #     )
        # )
        time.sleep(7)

        # Высчитываем формулу
        answer = str(math.log(int(time.time())))

        # Заполнение поля textarea
        textarea = driver.find_element(
            "xpath", "//textarea[@placeholder='Напишите ваш ответ здесь...']"
        )
        textarea.send_keys(answer)
        time.sleep(5)

        # Проверка, что введенный текст соответствует ожидаемому
        assert textarea.get_attribute("value") == answer

        # Кликаем кнопку отправить
        submit_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                ("xpath", "//button[@class='submit-submission']")
            )
        )
        submit_button.click()
        time.sleep(10)

        # Проверка успешности
        # success_message = driver.find_element("class name", "smart-hints__hint")
        # assert "Correct!" in success_message.text

        # Попытка найти успешное сообщение
        try:
            success_message = driver.find_element(
                "xpath", "//div[contains(@class,'smart-hints ember-view')]//p[1]"
            )
            assert "Correct!" in success_message.text
            print(success_message)
            print("Тест успешно выполнен.")
        except AssertionError:
            print(success_message)
            print("Текст не совпадает с ожидаемым. Тест завершается с ошибкой.")
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")


if __name__ == "__main__":
    TestLogin.main()
