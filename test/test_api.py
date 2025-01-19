import requests
import allure
from heders import URL_API, HEADERS


@allure.title("Поиск видео")
@allure.description("Тест на поиск видео по ID")
@allure.id(1)
@allure.severity("Критический")
def test_search_content_by_title():

    with allure.step("Вводим запрос GET и ID филма"):
        response = requests.get(
            f"{URL_API}movie/search?page=1&limit=10&query=%D1%82%D0%B5%D1%80%D0%BC%D0%B8%D0%BD%D0%B0%D1%82%D0%BE%D1%80", headers=HEADERS)

    with allure.step("Проверка ответа"):
        assert response.status_code == 200


@allure.title("Невалидный поиск видео")
@allure.description("Тест на поиск видео по несуществующему ID")
@allure.id(2)
@allure.severity("Критический")
def test_search_content_id_out_of_bounds():

    with allure.step("Отправляем GET запрос с несуществующим ID"):
        response = requests.get(f"{URL_API}/movie/11111", headers=HEADERS)

    with allure.step("Проверка ответа"):
        assert response.status_code == 200


@allure.title("Поиск видео с рейтингом 5")
@allure.description("Тест на поиск видео по рейтингу")
@allure.id(3)
@allure.severity("Критический")
def test_search_content_by_rating():

    with allure.step("Отправка GET запроса с указанием рейтинга"):
        response = requests.get(
            f"{URL_API}/movie?page=1&limit=10&rating.kp=5", headers=HEADERS)

    with allure.step("Проверка ответа"):
        assert response.status_code == 200


@allure.title("Поиск видео по году")
@allure.description("Тест на поиск видео по году выпуска")
@allure.id(4)
@allure.severity("Критический")
def test_search_content_type_and_year():

    with allure.step("Отправка GET запроса с указанием года выпуска"):
        response = requests.get(
            f"{URL_API}/movie?page=1&limit=10&typeNumber=3&year=2024", headers=HEADERS)

    with allure.step("Проверка ответа"):
        assert response.status_code == 200


@allure.title("Поиск актера")
@allure.description("Тест по поиску актера")
@allure.id(3)
@allure.severity("Критический")
def test_search_person_by_name():

    with allure.step("Вводим запрос GET с названием видео"):
        response = requests.get(
            f"{URL_API}/person/search?page=1&limit=10&query=%D0%91%D0%B5%D0%B7%D1%80%D1%83%D0%BA%D0%BE%D0%B2", headers=HEADERS)

    with allure.step("Проверка ответа"):
        assert response.status_code == 200
