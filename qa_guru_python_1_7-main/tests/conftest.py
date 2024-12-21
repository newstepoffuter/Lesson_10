import pytest
from selene import browser, be



@pytest.fixture(scope='session', autouse=True)
def browser_settings():
    browser.config.driver.maximize_window()
    browser.config.base_url = "https://github.com"

    yield
    browser.quit()