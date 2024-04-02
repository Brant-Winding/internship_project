from pages.base_page import Page
from pages.main_page import MainPage
from pages.settings_page import SettingsPage
from pages.company_connect_page import CompanyConnectPage


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.settings_page = SettingsPage(driver)
        self.company_connect_page = CompanyConnectPage(driver)

