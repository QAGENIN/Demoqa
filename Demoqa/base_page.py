import allure
from selene import browser, Element
from selene.support.conditions import have
from selenium.webdriver.support import expected_conditions

from Demoqa.page_object import resources


class BasePage:
    def open(self, url):
        browser.open(url)
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

        # browser.execute_script(
        #     "document.getElementById('fixedban').style.display = 'none'"
        # )
        # browser.execute_script(
        #     "document.getElementById('fixedban').style.display = 'none'"
        # )

    @allure.step('Сделать клик по {selector}')
    def click(self, selector):
        browser.element(selector).click()
        return self

    @allure.step('Сделать клик по {selector} имеющий текст {text}')
    def click_on_element_by_text(self, selector, text):
        browser.all(selector).element_by(have.exact_text(text))
        browser.element(selector).click()
        return self

    @allure.step('Ввести {text} в поле {selector}')
    def type(self, selector, text):
        browser.element(selector).type(text)
        return self

    def type_and_press_enter(self, selector, text):
        browser.element(selector).type(text).press_enter()
        return self

    def set_value(self, selector, value):
        browser.element(selector).send_keys(resources.path(value))
