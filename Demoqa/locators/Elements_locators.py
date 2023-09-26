from selene import browser
from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    INPUT_FULL_NAME = (By.XPATH, "//input[@id='userName']")
    INPUT_EMAIL = (By.XPATH, "//input[@id='userEmail']")
    INPUT_CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    INPUT_PERMANENT_ADDRESS = (By.XPATH, "//textarea[@id='permanentAddress']")
    BUTTON_SUBMIT = (By.XPATH, "//button[@id='submit']")
    JS_FULL_NAME = "#userName"

    CREATED_FULL_NAME = (By.XPATH, "//p[@id='name']")
    CREATED_EMAIL = (By.XPATH, "//p[@id='email']")
    CREATED_CURRENT_ADDRESS = (By.XPATH, "//p[@id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = (By.XPATH, "//p[@id='permanentAddress']")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.XPATH, '//button[@title="Expand all"]')
    TITLE_LIST = (By.XPATH, '//span[@class="rct-title"]')
    CHECK_BOX_LIST = (By.XPATH, '//span[@class="rct-checkbox"]')
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    OUTPUT_RESULT = (By.XPATH, '//span[@class="text-success"]')

    TITLE_LIST_TEXT = './/ancestor::span[@class="rct-text"]'
