import pytest
import allure
from selenium import webdriver
from urls import Urls
from pages.main_page import MainPage
from data.main_page_data import expected_answers


class TestMainPage:
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize("question_index", range(8))
    @allure.title('Проверка появления соответствующиго ответа при нажатии на вопрос')
    def test_answer_to_question(self, question_index):

        # перешли на страницу тестового приложения
        self.driver.get(Urls.base_url)

        # создай объект класса домашней страницы
        main_page = MainPage(self.driver)
        main_page.take_cookies()

        # Получаем ответ на вопрос
        answer_text = main_page.question_and_answer(question_index)

        expected_answer = expected_answers[question_index]

        # Делаем проверку, что полученное значение совпадает c ожидаемым
        assert answer_text == expected_answer

    @classmethod
    def teardown_class(cls):
        # Удаляем все куки
        cls.driver.delete_all_cookies()
        # Закрываем браузер
        cls.driver.quit()