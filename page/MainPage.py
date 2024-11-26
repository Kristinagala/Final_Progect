import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from configuration.ConfigProvider import ConfigProvier


class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        base_url = ConfigProvier().get("ui", "base_url")
        self.__driver.get(base_url)

    @allure.step("Найти поле Поиск")
    def search_field(self) -> None:
        """Этот метод находит поле 'Поиск'"""
        return self.__driver.find_element(
            By.CSS_SELECTOR, "input[name='kp_query']")

    @allure.step("Поиск фильма {title}")
    def search(self, title: str) -> None:
        """Этот метод передает поле 'Поиск' название фильма"""
        film = self.__driver.find_element(
            By.CSS_SELECTOR, "input[name='kp_query']")
        film.send_keys(title, Keys.RETURN)

    @allure.step("Получить название вкладки")
    def get_title_tab(self) -> str:
        """Этот метод возвращает название текущей вкладеи"""
        return self.__driver.title

    @allure.step("Получить текст сообщения")
    def get_empty_result_massage(self) -> str:
        """Этот метод возвращает текст сообщения"""
        h2 = self.__driver.find_element(
            By.XPATH, "//*[@id='block_left_pad']/div/table/tbody/tr[1]/td/h2")
        return h2.text

    @allure.step("Получить название фильма {title} из элемента")
    def search_by_movie_title(self, title: str) -> str:
        """Этот метод возвращает название фильма"""
        self.search(title)
        self.__driver.find_element(
            By.CSS_SELECTOR, "a[href='/film/3442/sr/1/']").click()
        name_film = self.__driver.find_element(
            By.XPATH,
            (
                "//*[@id='__next']/div[1]/div[2]/main/div[1]/div[2]/div/"
                "div[3]/div/div/div[1]/div[1]/div/div[1]/h1/span"
            )
        )
        return name_film.text

    @allure.step("Найти страницу актера, главной роли в фильме {title}")
    def get_actor(self, title: str):
        """Этот метод возвращает ссылку на актера"""
        self.search_by_movie_title(title)
        self.__driver.find_element(
            By.CSS_SELECTOR, "a[href='/film/3442/cast/']").click()
        try:
            WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH, "//a[contains(text(), 'Брэд Питт')]")))
        except TimeoutException:
            print("Время вышло")

        actor = self.__driver.find_element(
            By.XPATH, "//a[contains(text(), 'Брэд Питт')]")
        return actor
