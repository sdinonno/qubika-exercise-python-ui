from seleniumpagefactory.Pagefactory import PageFactory
from pages.base_page import BasePage


class GoogleResultPage(PageFactory, BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        'search_textarea': ('ID', 'APjFqb'),
        'suggested_option': ('ID', 'fprsl'),
        'first_result': ('CSS', '#search .Z26q7c.UK95Uc.jGGQ5e:first-child h3'),
        'images_button': ('XPATH', '//span[contains(text(), "Imágenes")]/parent::div/parent::a')
    }

    def get_textarea_text(self):
        return self.search_textarea.get_text()

    def get_suggested_option_text(self):
        return self.suggested_option.text

    def open_suggested_option(self):
        url = self.suggested_option.get_attribute('href')
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.navigate_to(url)

    def get_result_title(self):
        return self.first_result.text

    def click_images(self):
        self.images_button.click()
