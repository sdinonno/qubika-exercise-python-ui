from seleniumpagefactory import PageFactory

from pages.base_page import BasePage


class GoogleImagesResultPage(PageFactory, BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        'images_button': ('XPATH', '//div/span[contains(text(), "Imágenes")]')
    }

    def is_images_button_selected(self):
        return self.images_button.is_selected()
