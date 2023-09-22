from webdriver_manager.chrome import ChromeDriverManager
import time

link = "http://selenium1py.pythonanywhere.com//catalogue/coders-at-work_207/"


def test_have_button_add_to_card(driver):
    driver.get(link)
    button_value = driver.find_element(
        "xpath", "(//button[@type='submit'])[2]"
    ).get_attribute("value")
    print(button_value)
    # Ожидаемые значения для разных языков интерфейса
    expected_values = ["Añadir al carrito", "Ajouter au panier"]

    # Проверка, что значение находится в ожидаемых значениях
    assert button_value in expected_values
    time.sleep(10)
