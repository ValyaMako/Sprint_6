from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Ждём появление элемента
    def wait_for_element_to_be_presence(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    # Ждём пока элемент станет видимым
    def wait_for_element_to_be_visibility(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    # Ждём пока элемент станет кликабельныи
    def wait_for_element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))

    # Скролл до элемента
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # Ищем элемент
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    # Ищем элементы
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    # Клик по элементу
    def click(self, element):
        element.click()

    # Кликаем на элемент по локатору
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    # Получение текста элемента по локатору
    def get_text_of_element_by_locator(self, locator):
        return self.find_element(locator).text

    # Получение текста элемента
    def get_text_of_element(self, element):
        return element.text

    # Заполняем поле данными
    def data_entry(self, locator, data):
        self.wait_for_element_to_be_visibility(locator).send_keys(data)
