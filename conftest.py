import pytest
from datetime import datetime, timedelta
from selenium import webdriver
from urls import Urls


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.base_url)
    yield driver
    driver.delete_all_cookies()
    driver.quit()

# Определяем завтрашнюю дату и возвращаем её в формате "дд.мм.гггг"
@pytest.fixture(scope="function")
def tomorrow():
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d.%m.%Y")
    return tomorrow

