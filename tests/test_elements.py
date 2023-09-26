import allure
from Demoqa.page_object.Elements.text_box_page import TextBoxPage
from Demoqa.page_object.forms.student_registration_form_page import RegistrationPage


@allure.step('Test Text Box')
def test_text_box(setup_browser):
    text_box_page = TextBoxPage()
    text_box_page.open('text-box')
    text_box_page.filled_all_fields()
    text_box_page.check_filled_all_fields()


@allure.step('Test Practice From')
def test_practice_form():
    registration_page = RegistrationPage()
    registration_page.open('automation-practice-form')
    registration_page.filled_all_fields()
    registration_page.should_have_registred()
