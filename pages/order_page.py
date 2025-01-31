from datetime import datetime, timedelta
import random
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.base_page_locators import BasePageLocators


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    # Ожидаем появление заголовка "Для кого"
    def wait_for_header_for_whom(self):
        self.wait_for_element_to_be_presence(self.locators.header_for_whom)

    # Вводим имя, фамилию,адрес в форме "Для кого самокат"
    def fill_fields_for_whom(self, name, surname, address):
        self.data_entry(self.locators.input_name, name)
        self.data_entry(self.locators.input_surname, surname)
        self.data_entry(self.locators.input_address, address)

    # Нажимаем на поле "Станция метро"
    def click_on_input_metro_station(self):
        self.click_on_element(self.locators.input_station)

    # Ожидаем появления выпадающего списка со станциями метро
    def wait_for_station_list(self):
        self.wait_for_element_to_be_visibility(self.locators.list_stations)

    # Кликаем на станцию метро
    def click_on_station(self):
        self.click_on_element(self.locators.station)

    # Шаг на заполнение поля "Станция метро"
    def choice_metro_station(self):
        self.click_on_input_metro_station()
        self.wait_for_station_list()
        self.click_on_station()

    # Вводим номер телефона
    def fill_fields_for_whom_phone(self, number):
        self.data_entry(self.locators.input_phone, number)

    # Ожидаем, пока кнопка "Далее" станет кликабельной
    def wait_for_button_next_to_be_clickable(self, ):
        self.wait_for_element_to_be_clickable(self.locators.button_next)

    # Кликаем на кнопку "Далее"
    def click_on_button_next(self):
        self.click_on_element(self.locators.button_next)

    # Шаг для кнопки "Далее"
    def wait_and_click_on_button_next(self):
        self.wait_for_button_next_to_be_clickable()
        self.click_on_button_next()

    # Шаг для заполнения формы "Для кого самокат"
    def form_for_whom(self, name, surname, address, number):
        self.fill_fields_for_whom(name, surname, address)
        self.choice_metro_station()
        self.fill_fields_for_whom_phone(number)
        self.wait_and_click_on_button_next()


    # Ждем появления формы "Про аренду"
    def wait_for_header_about_rent(self):
        self.wait_for_element_to_be_presence(self.locators.header_about_rent)

    # Кликаем в поле календарь
    def click_on_calendar(self):
        self.click_on_element(self.locators.input_when)

    # Определяем дату завтрашнего дня и вводим её в поле
    def fill_tomorrow_date(self):
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d.%m.%Y")
        self.data_entry(self.locators.input_when, tomorrow)

    # Находим в календаре кнопку с датой завтрашнего дян и кликаем на неё
    def choice_selected_day_in_calendar(self):
        self.wait_for_element_to_be_clickable(self.locators.selected_day)
        self.click_on_element(self.locators.selected_day)

    # Шаг для заполнения поле "Когда привезти самокат"
    def field_when(self):
        self.click_on_calendar()
        self.fill_tomorrow_date()
        self.choice_selected_day_in_calendar()

    # Нажимаем на поле "Срок аренды"
    def click_on_input_rental_term(self):
        self.click_on_element(self.locators.input_rental_term)

    # Ждем появление выпадающего списка
    def wait_for_number_of_days_list(self):
        self.wait_for_element_to_be_presence(self.locators.list_of_days)

    # Выбираем срок аренды
    def choice_term_of_rent(self):
        self.click_on_element(self.locators.two_days)

    # Шаг выбор срока аренды
    def choice_rental_time(self):
        self.click_on_input_rental_term()
        self.wait_for_number_of_days_list()
        self.choice_term_of_rent()

    # Выбираем цвет самоката
    def choice_color(self):
        colors = self.find_elements(self.locators.checkboxes_of_color)
        random_color = random.choice(colors)
        self.click(random_color)

    # Вводим комментарий
    def input_comment(self, comment):
        self.data_entry(self.locators.input_comment, comment)

    # Ожидаем, пока кнопка "Заказать" станет кликабельным
    def wait_order_button_to_be_clickable(self):
        self.wait_for_element_to_be_clickable(self.locators.order_button)

    # Кликаем на кнопку "Заказать"
    def click_order_button(self):
        self.click_on_element(self.locators.order_button)

    # Шаг заполнение формы "Про аренду"
    def form_about_rent(self, comment):
        self.field_when()   # ВВодим дату доставки
        self.choice_rental_time()      # Выбираем срок аренды самоката
        self.choice_color()   # Выбираем цвет самоката
        self.input_comment(comment)     # Заполняем поле "Комментарий"
        self.wait_order_button_to_be_clickable()
        self.click_order_button()       # Кликаем на кнопку "Заказать"

    # Ожидаем появлением поп-апа "Хотите оформить заказ"
    def wait_for_pop_up_you_want(self):
        self.wait_for_element_to_be_presence(self.locators.pop_up_you_want)

    # Ожидаем кликабельности кнопки "Да"
    def wait_for_button_yes_to_be_clickable(self):
        self.wait_for_element_to_be_clickable(self.locators.button_yes)

    # Кликаем на кнопку "Да"
    def click_button_yes(self):
        self.click_on_element(self.locators.button_yes)

    # Шаг подтверждения заказа
    def order_confirmation(self):
        self.wait_for_pop_up_you_want()
        self.wait_for_button_yes_to_be_clickable()
        self.click_button_yes()

    # Ожидаем появление поп-апа "Заказ оформлен"
    def wait_for_pop_up_order_issued(self):
        self.wait_for_element_to_be_presence(self.locators.pop_up_order_issued)

    # Получаем текст поп-апа "Заказ оформлен"
    def text_of_pop_up_order_issued(self):
        return self.get_text_of_element_by_locator(self.locators.pop_up_order_issued)

    # Шаг полного заполнения формы заказа и его подтверждения
    def all_flow_of_scooter_order(self, name, surname, address, number, comment):
        self.wait_for_header_for_whom()
        self.form_for_whom(name, surname, address, number)
        self.form_about_rent(comment)
        self.order_confirmation()
        self.wait_for_pop_up_order_issued()
        return self.text_of_pop_up_order_issued()

    # Нажатие на лого "Самокат"
    def click_on_logo_scooter(self):
        self.wait_for_element_to_be_clickable(BasePageLocators.link_logo_scooter)
        self.click_on_element(BasePageLocators.link_logo_scooter)