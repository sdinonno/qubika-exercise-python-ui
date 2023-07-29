from seleniumpagefactory.Pagefactory import PageFactory
from base_page import BasePage

class ResultPage(PageFactory, BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {}