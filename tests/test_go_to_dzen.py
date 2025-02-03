import allure
from conftest import driver
from urls import Urls
from pages.main_page import MainPage

class TestGoToDzen:

    @allure.title('Проверка открытия в новом окне главной страницы Дзена при нажатии на логотип Яндекса')
    def test_go_to_dzen(self, driver):

        main_page = MainPage(driver)
        main_page.click_on_logo_ya()
        main_page.go_to_dzen()
        expected_new_url = Urls.dzen_url
        assert driver.current_url == expected_new_url

