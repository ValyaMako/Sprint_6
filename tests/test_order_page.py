import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
from data.order_page_data import *
from conftest import *


class TestOrderPage:

    @allure.title('Проверка оформления заказа, переходя в форму заказа по кнопке "Заказать" вверху страницы')
    def test_order_page_by_click_on_button_in_header(self, driver, tomorrow):
        user = users[0]

        main_page = MainPage(driver)     # Создали объект класса домашней страницы
        main_page.take_cookies()     # Приняли куки
        main_page.wait_and_click_on_button_in_header()     # Кликаем на кнопку "Заказать" вверху старницы
        order_page = OrderPage(driver)     # Создаем объект класса формы заказа
        number_of_order = order_page.all_flow_of_scooter_order(user["name"], user["surname"], user["address"], user["number"], tomorrow, user["comment"])
        assert keywords in number_of_order

    @allure.title('Проверка оформления заказа, переходя в форму заказа по кнопке "Заказать" внизу страницы')
    def test_order_page_by_click_on_button_bellow(self, driver, tomorrow):
        user = users[1]

        main_page = MainPage(driver)     # Создали объект класса домашней страницы
        main_page.take_cookies()     # Приняли куки
        main_page.wait_and_click_on_button_below()      # Кликаем по кнопке "Заказать" вверху старницы
        order_page = OrderPage(driver)      # Создаем объект класса формы заказа
        number_of_order = order_page.all_flow_of_scooter_order(user["name"], user["surname"], user["address"], user["number"], tomorrow, user["comment"])
        assert keywords in number_of_order
