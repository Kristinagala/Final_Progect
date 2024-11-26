import allure
from page.MainPage import MainPage
from page.PageTop250 import PageTop250


def test_search_field_is_displayed(browser):
    main_page = MainPage(browser)
    result = main_page.search_field()
    with allure.step("Проверить наличие поиска на странице"):
        assert result.is_displayed(), "Поле поиска не отображается на странице"


def test_search_by_name(browser, test_data: dict):
    movie_title = test_data.get("movie_title")
    main_page = MainPage(browser)
    name_film = main_page.search_by_movie_title(movie_title)
    with allure.step("Проверить, что названия фильмов совпадают"):
        assert name_film == "Троя (2004)"


def test_number_of_movies_per_page(browser):
    page_250 = PageTop250(browser)
    films = page_250.sum_films()
    with allure.step("Проверить, что на странице 50 фильмов"):
        assert len(films) == 50


def test_check_current_tab_title(browser):
    page_250 = PageTop250(browser)
    page_250.open_list_top_250()
    current_tab = page_250.get_title_tab()
    with allure.step("Проверить название вкладки"):
        assert "250 лучших фильмов — Кинопоиск" == current_tab


def test_check_page_title(browser):
    main_page = MainPage(browser)
    page_title = main_page.get_title_tab()
    with allure.step("Проверить заголовок страницы"):
        try:
            assert (
                "Кинопоиск. Онлайн кинотеатр."
                "Фильмы сериалы мультфильмы и энциклопедия"
                in page_title
            )
        except AssertionError:
            pass


def test_element_link(browser, test_data: dict):
    movie_title = test_data.get("movie_title")
    main_page = MainPage(browser)
    actor = main_page.get_actor(movie_title)
    with allure.step("Проверить, что эдемент содержит ссылку"):
        assert actor.get_attribute("href"), "Элемент не содержит ссылки!"


def test_empty_search_result(browser, test_data: dict):
    main_page = MainPage(browser)
    not_title = test_data.get("not_title")
    main_page.search(not_title)
    result_page = main_page.get_empty_result_massage()
    with allure.step("Проверить наличие сообщения"):
        assert (
            result_page == "К сожалению, по вашему запросу"
            " ничего не найдено..."
        )


def test_current_url(browser):
    page_250 = PageTop250(browser)
    page_250.open_list_top_250()
    with allure.step("Проверить url"):
        assert page_250.get_current_url().endswith("/lists/movies/top250/")
