import allure
from selene import browser
from selene.support.conditions import have

from Demoqa.base_page import BasePage
from Demoqa.locators.Elements_locators import TextBoxPageLocators as locator
from Demoqa.user_data.users import CreateTestUser


class TextBoxPage(BasePage):
    def __init__(self):
        super().__init__()

    @allure.step('Filled all fields')
    def filled_all_fields(self):
        self.type(locator.INPUT_FULL_NAME, CreateTestUser.name)
        self.type(locator.INPUT_EMAIL, CreateTestUser.email)
        self.type(locator.INPUT_CURRENT_ADDRESS, CreateTestUser.current_address)
        self.type(locator.INPUT_PERMANENT_ADDRESS, CreateTestUser.permanent_address)
        self.click(locator.BUTTON_SUBMIT)

    @allure.step('Check fill all fields')
    def check_filled_all_fields(self):
        browser.element(locator.CREATED_FULL_NAME).should(
            have.text(CreateTestUser.name)
        )
        browser.element(locator.CREATED_EMAIL).should(have.text(CreateTestUser.email))
        browser.element(locator.CREATED_CURRENT_ADDRESS).should(
            have.text(CreateTestUser.current_address)
        )
        browser.element(locator.CREATED_PERMANENT_ADDRESS).should(
            have.text(CreateTestUser.permanent_address)
        )
