from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    # Нажатие на лого "Яндекс"
    def click_on_logo_ya(self):
        self.wait_for_element_to_be_clickable(BasePageLocators.link_logo_ya)
        self.click_on_element(BasePageLocators.link_logo_ya)

    # Ждем пока кнопка "да все привыкли" появится на странице
    def wait_for_button_everyone_used_to_to_be_presence(self):
        self.wait_for_element_to_be_presence(self.locators.button_everyone_used_to)

    # Ждем пока кнопка "да все привыкли" станет кликабельной
    def wait_for_button_everyone_used_to_to_be_clickable(self):
        self.wait_for_element_to_be_clickable(self.locators.button_everyone_used_to)

    # Кликаем по кнопке "да все привыкли"
    def click_on_button_everyone_used_to(self):
        self.click_on_element(self.locators.button_everyone_used_to)

    # Шаг для нажатия по кнопке "да все привыкли"
    def take_cookies(self):
        try:
            self.wait_for_button_everyone_used_to_to_be_presence()
            self.wait_for_button_everyone_used_to_to_be_clickable()
            self.click_on_button_everyone_used_to()
        except Exception as e:
            print("Нет указанной кнопки для куков:", str(e))

    # Скроллим до блока с вопросами
    def scroll_to_question(self):
        self.scroll_to_element(self.locators.main_questions)

    # Ожидаем, пока вопрос станет кликабельным
    def wait_for_question_to_be_clickable(self, question_index):
        questions = self.find_elements(self.locators.question)
        self.wait_for_element_to_be_clickable(questions[question_index])

    # Кликаем на вопрос
    def click_on_question(self, question_index):
        questions = self.find_elements(self.locators.question)
        self.click(questions[question_index])

    # Получаем текст ответа
    def get_answer_text(self, question_index):
        answers = self.find_elements(self.locators.answer)
        return self.get_text_of_element(answers[question_index])

    # Шаг для получения ответа по клику на вопрос
    def question_and_answer(self, question_index):
        self.scroll_to_question()
        self.wait_for_question_to_be_clickable(question_index)
        self.click_on_question(question_index)
        return self.get_answer_text(question_index)

    # Ожидаем, пока кнопка "Заказать" станет кликабельной
    def wait_for_button_in_header_to_be_clickable(self):
        self.wait_for_element_to_be_clickable(self.locators.button_on_header)

    # Кликаем на кнопку "Заказать"
    def click_on_button_in_header(self):
        self.click_on_element(self.locators.button_on_header)

    # Шаг для кнопки "Заказать" в шапке страницы
    def wait_and_click_on_button_in_header(self):
        self.wait_for_button_in_header_to_be_clickable()
        self.click_on_button_in_header()

    # Скроллим до кнопки "Заказать" внизу страницы
    def scroll_to_button_bellow(self):
        self.scroll_to_element(self.locators.button_bellow)

    # Ожидаем, пока кнопка "Заказать" внизу страницы станет кликабельной
    def wait_for_button_bellow_to_be_clickable(self):
            self.wait_for_element_to_be_clickable(self.locators.button_bellow)

    # Кликаем на кнопку "Заказать" внизу страницы
    def click_on_button_bellow(self):
         self.click_on_element(self.locators.button_bellow)

    # Шаг для кнопки "Заказать" внизу страницы
    def wait_and_click_on_button_bellow(self):
        self.scroll_to_button_bellow()
        self.wait_for_button_bellow_to_be_clickable()
        self.click_on_button_bellow()
