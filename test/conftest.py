import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from api.film_api import FilmApi
from configuration.ConfigProvider import ConfigProvier
from test_data.DataProvider import DataProvier


@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        timeout = ConfigProvier().getint("ui", "timeout")
        browser = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
        browser.implicitly_wait(timeout)
        browser.maximize_window()
        yield browser
    with allure.step("Закрыть браузер"):
        browser.quit()


@pytest.fixture
def api_film() -> FilmApi:
    base_url = ConfigProvier().get("api", "base_url")
    return FilmApi(base_url)


@pytest.fixture
def test_data():
    return DataProvier()


@pytest.fixture
def head():
    my_headers = DataProvier().get_headers()
    return my_headers
