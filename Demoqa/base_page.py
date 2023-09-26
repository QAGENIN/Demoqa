import allure
from selene import browser, Element
from selene.core.condition import Condition
from selenium.webdriver.support import expected_conditions


class BasePage:
    def open(self, url):
        browser.open(url)
        browser.execute_script(
            "document.getElementById('fixedban').style.display = 'none'"
        )
        browser.execute_script(
            "document.getElementById('fixedban').style.display = 'none'"
        )

    @allure.step('Сделать клик по {selector}')
    def click(self, selector):
        browser.element(selector).wait_until(
            expected_conditions.element_to_be_clickable(mark=Element)
        )
        browser.element(selector).click()
        return self

    @allure.step('Ввести {text} в поле {selector}')
    def type(self, selector, text):
        browser.element(selector).type(text)
        return self
