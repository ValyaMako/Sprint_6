import allure
from conftest import driver
from urls import Urls
from pages.order_page import OrderPage
from pages.main_page import MainPage

class TestGoToMainPage:

    @allure.title('Проверка перехода на главную страницу при нажатии на логотип "Самаката" на странице заказа')
    def test_go_to_main_page_from_order_page(self, driver):

        main_page = MainPage(driver)     # Создаём объект класса домашней страницы
        main_page.wait_and_click_on_button_in_header()      # Клик на кнопку "Заказать" вверху старницы
        order_page = OrderPage(driver)     # Создаем объект класса формы заказа
        order_page.click_on_logo_scooter()      # Клик на кнопку лого Самоката
        main_page = MainPage(driver)  # Создаем новый объект класса главной старницы
        assert driver.current_url == Urls.base_url    # Проверяем, что URL текущей страницы равен URL главной страницы
