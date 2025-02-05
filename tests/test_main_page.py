import pytest
import allure
from conftest import driver
from pages.main_page import MainPage
from data.main_page_data import expected_answers


class TestMainPage:

    @pytest.mark.parametrize("question_index", range(8))
    @allure.title('Проверка появления соответствующиго ответа при нажатии на вопрос')
    def test_answer_to_question(self, driver, question_index):

        main_page = MainPage(driver)     # Создаём объект класса домашней страницы
        main_page.take_cookies()     # Принимаем куки
        answer_text = main_page.question_and_answer(question_index)     # Получаем текст ответа по клику на вопрос
        expected_answer = expected_answers[question_index]     # Определяем ожидаемый ответ по индексу вопроса, на который кликали
        assert answer_text == expected_answer     # Делаем проверку, что полученный ответ совпадает c ожидаемым

