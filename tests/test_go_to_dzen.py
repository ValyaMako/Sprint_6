import allure
import time
from selenium import webdriver
from urls import Urls
from pages.main_page import MainPage



class TestGoOnMainPage:
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка открытия в новом окне главной страницы Дзена при нажатии на логотип Яндекса')
    def test_go_to_dzen(self):

        # перешли на страницу тестового приложения
        self.driver.get(Urls.base_url)

        # создай объект класса домашней страницы
        main_page = MainPage(self.driver)
        main_page.click_on_logo_ya()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        expected_new_url = Urls.dzen_url
        assert self.driver.current_url == expected_new_url

    @classmethod
    def teardown_class(cls):
        # Закрываем браузер
        cls.driver.quit()
