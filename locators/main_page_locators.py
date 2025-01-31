from selenium.webdriver.common.by import By

class MainPageLocators:
    button_everyone_used_to = By.ID, "rcc-confirm-button"
    main_questions = By.XPATH, "//div[text()='Вопросы о важном']"
    question = (By.CLASS_NAME, 'accordion__button')
    answer = (By.CLASS_NAME, 'accordion__panel')
    button_on_header = By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']"
    button_bellow = By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button[text()='Заказать']"


