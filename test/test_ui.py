import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from pages.PageObject import MainPage
from heders import BASE_URL


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def search_page(driver):
    driver.get(BASE_URL)
    return MainPage(driver)


@allure.title("Поиск видео по году выпуска")
@allure.description("Тест по поиску видео с указанием года выпуска")
@allure.id(1)
@allure.severity("Критический")
def test_search_by_year(search_page):

    with allure.step("Вводим год"):
        search_page.search_by_year(2001)

    with allure.step("Метод проверяет, что видео соответствует году"):
        year_element = search_page.wait_for_element(By.CLASS_NAME, "year")
        assert year_element.text == "2001 – 2010", f"Expected year to be 2001 – 2010, but got {
            year_element.text}"


@allure.title("Поиск фильма по названию")
@allure.description("Тест на поиск фильма по названию")
@allure.id(2)
@allure.severity("Критический")
def test_search_by_title(search_page):

    with allure.step("Вводим название фильма"):
        search_page.search_by_title("Анора")

    with allure.step("Метод проверяет, что видео соответствует названию фильма"):
        is_content_found = search_page.wait_for_element_with_text(
            By.CLASS_NAME, "gray", "Anora")
        assert is_content_found, "Expected to find content 'Anora'"


@allure.title("Невалидный поиск видео по названию")
@allure.description("Тест на поиск видео по несуществующему названию")
@allure.id(3)
@allure.severity("Критический")
def test_search_title_negativ(search_page):

    with allure.step("В методе указываем название фильма"):
        search_page.search_by_title("Кыоворывлорм")

    with allure.step("Метод проверяет, что система сообщит об отсутствии видео с несуществующим названием"):
        is_content_found = search_page.wait_for_element_with_text(
            By.CLASS_NAME, "textorangebig", "К сожалению, по вашему запросу ничего не найдено...")
        assert is_content_found, "К сожалению, по вашему запросу ничего не найдено..."


@allure.title("Поиск актера")
@allure.description("Выполнение теста на поиск видео по актеру")
@allure.id(5)
@allure.severity("Критический")
def test_search_by_actor(search_page):

    with allure.step("В методе указываем название фильма и имя актера"):
        search_page.search_by_actor("Гарри Потер", "Дэниэл Рэдклифф")

    with allure.step("Метод проверяет, что найденное видео соответствует указанному фильму и актеру"):
        is_content_found = search_page.wait_for_element_with_text(
            By.CLASS_NAME, "gray", "Harry Potter and the Sorcerer's Stone")
        assert is_content_found, "Expected to find content 'Harry Potter and the Sorcerer's Stone'"


@allure.title("Поиск видео по жанру")
@allure.description("Тест на поиск видео по жанру")
@allure.id(4)
@allure.severity("Критический")
def test_search_by_genre(search_page):

    with allure.step("В методе указываем жанр видео"):
        search_page.search_by_genre("фантастика")

    with allure.step("Метод проверяет, что найденное видео соответствует указанному жанру"):
        is_genre_found = search_page.wait_for_element_with_text(
            By.XPATH, "//span[@class='gray' and contains(., 'фантастика')]", "фантастика")
        assert is_genre_found, "Expected to find content with genre 'фантастика'"
