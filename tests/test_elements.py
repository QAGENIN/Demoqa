import allure
from Demoqa.page_object.Elements.text_box_page import TextBoxPage
from tests.conftest import browser_setting


@allure.step("Test Text Box")
def test_text_box(browser_setting):
    text_box_page = TextBoxPage()
    text_box_page.open('text-box')
    text_box_page.filled_all_fields()
    text_box_page.check_filled_all_fields()


# @allure.step("Test Check Box")
# def test_check_box(browser_setting):
#     check_box_page = CheckBoxPage()
#     check_box_page.open('checkbox')
#     check_box_page.check_in_boxes()
#     check_box_page.assert_checkbox_input_and_output()
