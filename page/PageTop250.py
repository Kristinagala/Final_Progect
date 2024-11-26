import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from configuration.ConfigProvider import ConfigProvier


class PageTop250:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        base_url = ConfigProvier().get("ui", "base_url")
        self.__driver.get(base_url)

    @allure.step("Получить список Топ250")
    def open_list_top_250(self) -> None:
        """Этот метод открывает страницу 'Топ250'"""
        self.__driver.find_element(
            By.CSS_SELECTOR,
            (
                "svg[class='styles_advancedSearchIconActive__4bcK9 "
                "styles_advancedSearchIcon__Zxjax']"
            )
        ).click()

        top250 = self.__driver.find_element(By.CSS_SELECTOR,
                                            "a[href='/level/20/']").click()
        return top250

    @allure.step("Получить название вкладки")
    def get_title_tab(self) -> str:
        """Этот метод возвращает название текущей вкладки"""
        return self.__driver.title

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        """Этот метод возвращает текущий URL"""
        return self.__driver.current_url

    @allure.step("Посчитать количество фильмов на странице")
    def sum_films(self) -> list[str]:
        """Этот метод возвращает все фильмы со страницы 'Топ250'"""
        self.open_list_top_250()
        films = self.__driver.find_elements(By.CSS_SELECTOR,
                                            "div[class='styles_root__ti07r']")
        return films
