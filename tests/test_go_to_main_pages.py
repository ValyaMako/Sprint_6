import allure
from selenium import webdriver
from urls import Urls
from pages.order_page import OrderPage
from pages.main_page import MainPage


class TestGoOnMainPage:
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка перехода на главную страницу при нажатии на логотип "Самаката" на странице заказа')
    def test_order_page(self):

        # перешли на страницу тестового приложения
        self.driver.get(Urls.base_url)

        # создай объект класса домашней страницы
        main_page = MainPage(self.driver)
        main_page.wait_and_click_on_button_in_header()

        # Создаем объект класса формы заказа
        order_page = OrderPage(self.driver)
        order_page.click_on_logo_scooter()

        # Создаем новый объект класса главной старницы
        main_page = MainPage(self.driver)

        assert self.driver.current_url == Urls.base_url

    @classmethod
    def teardown_class(cls):
        # Закрываем браузер
        cls.driver.quit()