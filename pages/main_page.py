from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page


class MainPage(Page):
    EMAIL = (By.ID, "email-2")
    PASSWORD = (By.ID, "field")
    CONTINUE_BTN = (By.LINK_TEXT, 'Continue')
    MENU_BTN = (By.CSS_SELECTOR, '[class="menu-button-wrapper w-inline-block"]')
    YOUR_COUNTRY = (By.ID, 'Your-country')
    COMPANY_NAME = (By.ID, 'Company-name-2')
    POSITION = (By.ID, 'Position')
    TEST_NAME = (By.ID, 'Director-name')
    TEST_NUMBER = (By.ID, 'Director-phone')
    AGENTS_IN_COMPANY = (By.ID, 'Amount-of-agents-in-company')
    EMAIL_2 = (By.ID, 'Email-2')

    def open_main(self):
        self.open('https://soft.reelly.io/sign-in')

    def login(self):
        self.input_text('test@example.com', *self.EMAIL)
        self.input_text('Test009.', *self.PASSWORD)
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BTN))
        self.click(*self.CONTINUE_BTN)
        sleep(3)

    def click_menu(self):
        self.wait.until(EC.visibility_of_element_located(self.MENU_BTN))
        self.wait.until(EC.element_to_be_clickable(self.MENU_BTN))
        self.find_element(*self.MENU_BTN)
        self.click(*self.MENU_BTN)
