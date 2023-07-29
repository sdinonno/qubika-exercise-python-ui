from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from util.file import File
from selenium.webdriver.support import expected_conditions as ec


class GoogleSearchPage(PageFactory, BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        'images_link': ('CSS', '.gb_z.gb_A a[href*="img"]'),
        'gmail_link': ('CSS', '.gb_z.gb_A a[href*="mail"]'),
        'google_products_button': ('CSS', 'a.gb_d[href*="products"]'),
        'access_button': ('CSS', '.gb_0d>a'),
        'search_text_area': ('ID', 'APjFqb'),
    }

    def load(self):
        file = File('data/config.json')
        self.navigate_to(file.get_property("url"))

    def perform_search(self, text):
        self.search_text_area.set_text(text + Keys.ENTER)

    def is_element_visible(self, element, timeout=10, poll=2):
        try:
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll)
            wait.until(ec.visibility_of(element))
            return True
        except TimeoutException:
            return False

    def is_menu_elements_present(self):
        images_visible = self.is_element_visible(self.images_link)
        gmail_visible = self.is_element_visible(self.gmail_link)
        products_visible = self.is_element_visible(self.google_products_button)
        access_visible = self.is_element_visible(self.access_button)

        return images_visible and gmail_visible and products_visible and access_visible
