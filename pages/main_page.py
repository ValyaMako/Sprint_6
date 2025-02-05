import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException
from urls import Urls

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step('Клик на логотип Яндекса')
    def click_on_logo_ya(self):
        self.wait_for_element_to_be_clickable(BasePageLocators.link_logo_ya)
        self.click_on_element(BasePageLocators.link_logo_ya)

    @allure.step('Ожидаем появления кнопки "да все привыкли" на странице')
    def wait_for_button_everyone_used_to_to_be_presence(self):
        self.wait_for_element_to_be_presence(self.locators.button_everyone_used_to)

    @allure.step('Ожидаем кликабельности кнопки "да все привыкли"')
    def wait_for_button_everyone_used_to_to_be_clickable(self):
        self.wait_for_element_to_be_clickable(self.locators.button_everyone_used_to)

    @allure.step('Клик по кнопке "да все привыкли"')
    def click_on_button_everyone_used_to(self):
        self.click_on_element(self.locators.button_everyone_used_to)

    @allure.step('Шаг для нажатия по кнопке "да все привыкли"')
    def take_cookies(self):
        try:
            self.wait_for_button_everyone_used_to_to_be_presence()
            self.wait_for_button_everyone_used_to_to_be_clickable()
            self.click_on_button_everyone_used_to()
        except NoSuchElementException:
            pass

    @allure.step('Скролл до блока с вопросами')
    def scroll_to_question(self):
        self.scroll_to_element(self.locators.main_questions)

    @allure.step('Ожидаем кликабельности вопроса')
    def wait_for_question_to_be_clickable(self, question_index):
        questions = self.find_elements(self.locators.question)
        self.wait_for_element_to_be_clickable(questions[question_index])

    @allure.step('Клик на вопрос')
    def click_on_question(self, question_index):
        questions = self.find_elements(self.locators.question)
        self.click(questions[question_index])

    @allure.step('Получаем текст ответа')
    def get_answer_text(self, question_index):
        answers = self.find_elements(self.locators.answer)
        return self.get_text_of_element(answers[question_index])

    @allure.step('Получение текста ответа по клику на вопрос')
    def question_and_answer(self, question_index):
        self.scroll_to_question()
        self.wait_for_question_to_be_clickable(question_index)
        self.click_on_question(question_index)
        return self.get_answer_text(question_index)

    @allure.step('Ожидаем кликабельности кнопки "Заказать" вверху страницы')
    def wait_for_button_in_header_to_be_clickable(self):
        self.wait_for_element_to_be_clickable(self.locators.button_on_header)

    @allure.step('Клик на кнопку "Заказать" вверху страницы')
    def click_on_button_in_header(self):
        self.click_on_element(self.locators.button_on_header)

    @allure.step('Шаг для клика по кнопке "Заказать" вверху страницы')
    def wait_and_click_on_button_in_header(self):
        self.wait_for_button_in_header_to_be_clickable()
        self.click_on_button_in_header()

    @allure.step('Скролл до кнопки "Заказать" внизу страницы')
    def scroll_to_button_below(self):
        self.scroll_to_element(self.locators.button_below)

    @allure.step('Ожидаем кликабельности кнопки "Заказать" внизу страницы')
    def wait_for_button_below_to_be_clickable(self):
            self.wait_for_element_to_be_clickable(self.locators.button_below)

    @allure.step('Клик на кнопку "Заказать" внизу страницы')
    def click_on_button_below(self):
         self.click_on_element(self.locators.button_below)

    @allure.step('Шаг для клика по кнопке "Заказать" внизу страницы')
    def wait_and_click_on_button_below(self):
        self.scroll_to_button_below()
        self.wait_for_button_below_to_be_clickable()
        self.click_on_button_below()

    @allure.step('Ожидание открытия главной страницы Дзена в новой вкладке')
    def go_to_dzen(self):
        self.wait_for_new_tab(2)    # Ожидаем открытие второй вкладки
        self.go_to_new_tab(-1)      # Открываем последнюю вкладку
        return self.wait_for_url_to_be(Urls.dzen_url)    # Возвращает True, если страница с ожидаемым URL загрузилась