from selenium.webdriver.common.by import By

class BasePageLocators:
    link_logo_scooter = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")   # Логотип Самоката
    link_logo_ya = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")    # Логотип Яндекс