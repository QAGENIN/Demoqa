import pytest
from selene import browser


@pytest.fixture(scope="function")
def browser_setting():
    browser.config.base_url = 'https://demoqa.com/'
