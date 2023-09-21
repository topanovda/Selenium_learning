import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeOptions
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox",
    )
    parser.addoption(
        "--language",
        action="store",
        default=None,
        help="Choose language: '--language=en' or '--language=ru'",
    )


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser_name")
    user_language = "none"  # Здесь задайте язык по умолчанию (например, "en")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = webdriver.ChromeOptions()
        if user_language != "none":
            options.add_experimental_option(
                "prefs", {"intl.accept_languages": user_language}
            )
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = Options()
        fp = webdriver.FirefoxProfile()
        if user_language != "none":
            options.set_preference("intl.accept_languages", user_language)
        driver = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield driver
    print("\nquit browser..")
    driver.quit()


# @pytest.fixture(scope="function")
# def driver(request):
#     browser_name = request.config.getoption("browser_name")
#     driver = None
#     if browser_name == "chrome":
#         print("\nstart chrome browser for test..")
#         driver = webdriver.Chrome()
#     elif browser_name == "firefox":
#         print("\nstart firefox browser for test..")
#         driver = webdriver.Firefox()
#     else:
#         raise pytest.UsageError("--browser_name should be chrome or firefox")
#     yield driver
#     print("\nquit browser..")
#     driver.quit()


# @pytest.fixture(scope="function")
# def driver():
#     print("\nstart browser for test..")
#     driver = webdriver.Chrome()
#     yield driver
#     print("\nquit browser..")
#     driver.quit()
