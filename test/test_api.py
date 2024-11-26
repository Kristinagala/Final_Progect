from api.film_api import FilmApi
import allure


def test_get_films_by_year(api_film: FilmApi, test_data: dict):
    year = test_data.get("year")
    body = api_film.search_movies_by_year_of_release(year)
    with allure.step("Проверить год релиза фильма"):
        assert body["docs"][1]["year"] == int(year)


def test_get_films_by_title(api_film: FilmApi, test_data: dict):
    title = test_data.get("title")
    body = api_film.search_for_a_movie_by_title(title)
    with allure.step("Проверить название фильма"):
        assert body["docs"][0]["alternativeName"] == title


def test_get_actor_by_name(api_film: FilmApi, test_data: dict):
    name = test_data.get("name")
    body = api_film.search_for_a_movie_by_name_actor(name)
    with allure.step("Проверить имя актера"):
        assert body["docs"][0]["alternativeName"] == name


def test__get_films_by_genre(api_film: FilmApi, test_data: dict):
    genre = test_data.get("genre")
    body = api_film.search_for_a_movie_by_genre(genre)
    with allure.step("Проверить, фильмов в выдаче больше нуля"):
        assert len(body) > 0


def test_get_films_by_id(api_film: FilmApi, test_data: dict):
    id = test_data.get("id")
    body = api_film.search_for_a_movie_by_id(id)
    with allure.step("Проверить id фильма"):
        assert body["id"] == int(id)


def test_response_status(api_film: FilmApi):
    result = api_film.response_status()
    with allure.step("Проверить, что статус код=200"):
        assert result.status_code == 200


def test_request_without_authorization(api_film: FilmApi):
    result = api_film.request_without_authorization()
    with allure.step("Проверить, что статус код=401"):
        assert result.status_code == 401


def test_request_by_incorrect_id(api_film: FilmApi, test_data: dict):
    incorrect_id = test_data.get("incorrect_id")
    result = api_film.search_for_a_movie_by_id(incorrect_id)
    with allure.step("Проверить текст ошибки"):
        assert result["error"] == "Bad Request"


def test_request_by_incorrect_title_movie(api_film: FilmApi, test_data: dict):
    incorrect_title = test_data.get("incorrect_title")
    result = api_film.search_for_a_movie_by_title(incorrect_title)
    with allure.step("Проверить, что возвращается пустой список"):
        assert result["docs"] == []
