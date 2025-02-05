from selenium.webdriver.common.by import By

class OrderPageLocators:
    header_for_whom = By.XPATH, "//div[text()='Для кого самокат']"  # Заголовок "Для кого самокат"
    input_name = By.XPATH, "//input[@placeholder='* Имя']"          # Поле "Имя"
    input_surname = By.XPATH, "//input[@placeholder='* Фамилия']"   # Поле "Фамилия"
    input_address = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"  # Поле "Адрес"
    input_station = By.XPATH, "//input[@placeholder='* Станция метро']"  # Поле "Станция метро"
    list_stations = By.CLASS_NAME, "select-search__select"   # Выпадающий список со станциями метро
    station = By.XPATH, "//div[@class='select-search__select']//*[text()='Бульвар Рокоссовского']"  # Станция метро "Бульвар Рокоссовского"
    input_phone = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"   # Поле "Телефон"
    button_next = (By.XPATH, "//button[text()='Далее']")   # Кнопка "Далее"
    header_about_rent = By.XPATH, "//div[text()='Про аренду']"   # Заголовок "Про аренду"
    input_when = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"   # Поле "Когда привезти самокат"
    selected_day = By.XPATH, "//div[contains(@class, 'day--selected')]"
    input_rental_term = By.XPATH, "//div[@class='Dropdown-placeholder']"   # Поле "Срок аренды"
    list_of_days = By.XPATH, "//div[@class='Dropdown-menu']"   # Выпадающий список с количеством суток аренды
    two_days = By.XPATH, "//div[text()='двое суток' and @role='option']"   # Вариант количества дней аренды 'двое суток 'в выпадающем списке
    checkboxes_of_color = By.XPATH, "//input[@type='checkbox']"  # Чекбоксы для выбора цвета самоката
    input_comment = By.XPATH, "//input[@placeholder='Комментарий для курьера']"   # Поле "Комментарий"
    order_button = By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']"   # Кнопка "Заказать"
    pop_up_you_want = By.XPATH, "//div[text()='Хотите оформить заказ?']/.."    # Поп-ап "Хотите оформить заказ?"
    button_yes = By.XPATH, "//button[text()='Да']"  # Кнопка "Да"
    pop_up_order_issued = By.XPATH, "//div[text()='Заказ оформлен']/.."    # Поп-ап "Заказ оформлен"
