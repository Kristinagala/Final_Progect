import requests
import allure
from test_data.DataProvider import DataProvier

my_headers = DataProvier().get_headers()


class FilmApi:

    def __init__(self, url: str) -> None:
        self.url = url

    @allure.step("Найти фильм по году релиза {year}")
    def search_movies_by_year_of_release(self, year: str) -> dict:
        """Поиск по году выхода фильма"""
        resp = requests.get(self.url+'movie?year= '+year, headers=my_headers)
        return resp.json()

    @allure.step("Найти филь по названию {title}")
    def search_for_a_movie_by_title(self, title: str) -> dict:
        """Поиск по названию фильма"""
        resp = requests.get(
            self.url+'movie/search?page=1&limit=10&query= '+title,
            headers=my_headers)
        return resp.json()

    @allure.step("Нати актера по имени {name}")
    def search_for_a_movie_by_name_actor(self, name: str) -> dict:
        """Поиск по имени актера"""
        resp = requests.get(
            self.url+'movie/search?page=1&limit=10&query= '+name,
            headers=my_headers)
        return resp.json()

    @allure.step("Найти фильм по жанру {genre}")
    def search_for_a_movie_by_genre(self, genre: str) -> dict:
        """Поиск по жанру"""
        resp = requests.get(
            self.url+'movie/search?page=1&limit=10&query= '+genre,
            headers=my_headers)
        return resp.json()

    @allure.step("Найти фильм по {id}")
    def search_for_a_movie_by_id(self, id: str) -> dict:
        """Поиск по id фильма"""
        resp = requests.get(self.url+'movie/ '+id, headers=my_headers)
        return resp.json()

    @allure.step("Получить рандомный тайтл")
    def response_status(self) -> dict:
        """Получить рандомный тайтл из базы"""
        return requests.get(self.url+'movie/random', headers=my_headers)

    @allure.step("Отправить запрос без авторизации")
    def request_without_authorization(self) -> dict:
        """Запрос без авторизации"""
        return requests.get(self.url+'movie/random')
