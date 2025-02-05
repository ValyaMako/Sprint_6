import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание элемента на странице')
    def wait_for_element_to_be_presence(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))

    @allure.step('Ожидание видимости элемента')
    def wait_for_element_to_be_visibility(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))

    @allure.step('Ожидание кликабельности элемента')
    def wait_for_element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(locator))

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Поиск элементов')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Клик по переданному элементу')
    def click(self, element):
        element.click()

    @allure.step('Получение текста элемента по локатору')
    def get_text_of_element_by_locator(self, locator):
         return self.driver.find_element(*locator).text

    @allure.step('Получение текста переданного элемента')
    def get_text_of_element(self, element):
        return element.text

    @allure.step('Заполняем поле данными')
    def data_entry(self, locator, data):
        self.wait_for_element_to_be_visibility(locator).send_keys(data)

    @allure.step('Ожидание открытия новой вкладки')
    def wait_for_new_tab(self, number_of_tabs):
        return WebDriverWait(self.driver, 10).until(ec.number_of_windows_to_be(number_of_tabs))

    @allure.step('Переход на другую вкладку по индексу')
    def go_to_new_tab(self, index_of_tab):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[index_of_tab])

    @allure.step('Ожидание загрузки страницы по URL')
    def wait_for_url_to_be(self, new_url):
        return WebDriverWait(self.driver, 10).until(ec.url_to_be(new_url))

    @allure.step('Получение URL текущей страницы')
    def get_current_url(self):
        return self.driver.current_url