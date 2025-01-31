import allure
from selenium import webdriver
from urls import Urls
from pages.order_page import OrderPage
from pages.main_page import MainPage
from data.order_page_data import users


class TestOrderPage:
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка оформления заказа, переходя в форму заказа по кнопке "Заказать" вверху страницы')
    def test_order_page_by_click_on_button_in_header(self):
        user = users[0]
        # перешли на страницу тестового приложения
        self.driver.get(Urls.base_url)

        # создай объект класса домашней страницы
        main_page = MainPage(self.driver)
        main_page.take_cookies()

        # Кликаем по кнопке "Заказать" вверху старницы
        main_page.wait_and_click_on_button_in_header()

        # Создаем объект класса формы заказа
        order_page = OrderPage(self.driver)

        number_of_order = order_page.all_flow_of_scooter_order(user["name"], user["surname"], user["address"], user["number"], user["comment"])

        assert 'Номер заказа:' in number_of_order

    @allure.title('Проверка оформления заказа, переходя в форму заказа по кнопке "Заказать" внизу страницы')
    def test_order_page_by_click_on_button_bellow(self):
        # перешли на страницу тестового приложения
        self.driver.get(Urls.base_url)
        user = users[1]
        # создай объект класса домашней страницы
        main_page = MainPage(self.driver)
        main_page.take_cookies()

        # Кликаем по кнопке "Заказать" вверху старницы
        main_page.wait_and_click_on_button_bellow()

        # Создаем объект класса формы заказа
        order_page = OrderPage(self.driver)

        number_of_order = order_page.all_flow_of_scooter_order(user["name"], user["surname"], user["address"], user["number"], user["comment"])

        assert 'Номер заказа:' in number_of_order

    @classmethod
    def teardown_class(cls):
        # Удаляем все куки
        cls.driver.delete_all_cookies()
        # Закрываем браузер
        cls.driver.quit()
