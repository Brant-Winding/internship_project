from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page


class CompanyConnectPage(Page):
    YOUR_COUNTRY = (By.ID, 'Your-country')
    COMPANY_NAME = (By.ID, 'Company-name-2')
    POSITION = (By.ID, 'Position')
    TEST_NAME = (By.ID, 'Director-name')
    TEST_NUMBER = (By.ID, 'Director-phone')
    AGENTS_IN_COMPANY = (By.ID, 'Amount-of-agents-in-company')
    EMAIL_2 = (By.ID, 'Email-2')
    SEND_REQUEST_BTN = (By.CSS_SELECTOR, '[class ="purchase-access w-button"]')
    SUBSCRIPTION_BTN = (By.CSS_SELECTOR, '[class="step-button margin-bottom-8 w-button"]')

    def enter_test_info(self):
        self.input_text('USA', *self.YOUR_COUNTRY)
        self.input_text('MEFIME', *self.COMPANY_NAME)
        self.input_text('CFO', *self.POSITION)
        self.input_text('TEST-BRANT', *self.TEST_NAME)
        self.input_text('123+test+careerist', *self.TEST_NUMBER)
        self.input_text('10', *self.AGENTS_IN_COMPANY)
        self.input_text('test@example.com', *self.EMAIL_2)

    def verify_test_info(self):
        assert len(self.YOUR_COUNTRY) == len(self.YOUR_COUNTRY)
        assert len(self.COMPANY_NAME) == len(self.COMPANY_NAME)
        assert len(self.POSITION) == len(self.POSITION)
        assert len(self.TEST_NAME) == len(self.TEST_NAME)
        assert len(self.TEST_NUMBER) == len(self.TEST_NUMBER)
        assert len(self.AGENTS_IN_COMPANY) == len(self.AGENTS_IN_COMPANY)
        assert len(self.EMAIL_2) == len(self.EMAIL_2)
        sleep(2)

    def verify_request_button(self):
        self.driver.find_element(*self.SEND_REQUEST_BTN)
        self.wait.until(EC.presence_of_element_located(self.SEND_REQUEST_BTN))

    def verify_subscription_button(self):
        self.driver.find_element(*self.SUBSCRIPTION_BTN)
        self.wait.until(EC.presence_of_element_located(self.SUBSCRIPTION_BTN))
