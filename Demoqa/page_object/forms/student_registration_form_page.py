from selene import browser, have, be
from Demoqa.page_object import resources
import allure
from selene import browser
from selene.support.conditions import have
from Demoqa.user_data.users import test_user
from Demoqa.base_page import BasePage
from Demoqa.locators.Elements_locators import StudentRegistrationForm as locator


class RegistrationPage(BasePage):
    @allure.step('Filled all fields')
    def filled_all_fields(self):
        self.type(locator.INPUT_FIRST_NAME, test_user.first_name)
        self.type(locator.INPUT_LAST_NAME, test_user.last_name)
        self.type(locator.INPUT_EMAIL, test_user.email)
        self.click_on_element_by_text(locator.GENDER, test_user.gender)
        self.type(locator.MOBILE, test_user.mobile)
        self.fill_date_of_birth(test_user.date_of_birth)
        self.type_and_press_enter(locator.SUBJECT, test_user.subjects)
        self.click_on_element_by_text(locator.HOBBIES, test_user.hobbies)
        self.set_value(locator.PIC, test_user.picture)
        self.type(locator.INPUT_CURRENT_ADDRESS, test_user.address)
        self.fill_state(test_user.state)
        self.fill_city(test_user.city)
        self.click(locator.BUTTON_SUBMIT)
        return self

    @allure.step('Ввести в поле State - {text}')
    def fill_state(self, text):
        browser.element('#state').click()
        browser.all("#state div").element_by(have.exact_text(text)).click()
        return self

    @allure.step('Ввести в поле City - {text}')
    def fill_city(self, text):
        browser.element('#city').click()
        browser.all("#city div").element_by(have.exact_text(text)).click()
        return self

    def fill_date_of_birth(self, date):
        year = date.year
        month = date.month - 1
        day = date.strftime('%d')
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(
            f'.react-datepicker__year-select option[value="{year}"]'
        ).click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(
            f'.react-datepicker__month-select option[value="{month}"]'
        ).click()
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    @allure.step('Check fill all fields')
    def check_all_fields(self):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{test_user.first_name} {test_user.last_name}',
                f'{test_user.email}',
                f'{test_user.gender}',
                f'{test_user.mobile}',
                '{0} {1},{2}'.format(
                    test_user.date_of_birth.strftime("%d"),
                    test_user.date_of_birth.strftime("%B"),
                    test_user.date_of_birth.year,
                ),
                f'{test_user.subjects}',
                f'{test_user.hobbies}',
                f'{test_user.picture}',
                f'{test_user.address}',
                f'{test_user.state} {test_user.city}',
            )
        )

        browser.element('#closeLargeModal').click()
        browser.element('#firstName').should(be.blank)
