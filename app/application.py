from pages.base_page import Page
from pages.main_page import MainPage
from pages.company_connect_page import CompanyConnectPage


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.company_connect_page = CompanyConnectPage(driver)

