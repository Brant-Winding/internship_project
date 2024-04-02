from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page


class SettingsPage(Page):
    COMPANY_CONNECT_BTN = (By.XPATH, "//div[@class='settings-block-menu']"
                                     "//a[@class='button-link-menu w-inline-block']")
    # COMPANY_CONNECT_BTN = (By.CSS_SELECTOR, '[class="button-link-menu w-inline-block"]')

    def company_connect(self):
        self.wait.until(EC.visibility_of_element_located(self.COMPANY_CONNECT_BTN))
        self.wait.until(EC.element_to_be_clickable(self.COMPANY_CONNECT_BTN))
        self.find_element(*self.COMPANY_CONNECT_BTN)
        self.click(*self.COMPANY_CONNECT_BTN)
