from pages.images_search_page import GoogleImagesResultPage
from pages.search_page import GoogleSearchPage
from pages.result_page import GoogleResultPage


def test_perform_google_search(browser):
    search_page = GoogleSearchPage(browser)
    result_page = GoogleResultPage(browser)
    images_result_page = GoogleImagesResultPage(browser)
    phrase = "teesting"
    valid_suggested_phrase = "testing"

    search_page.load()
    assert search_page.driver.title == "Google"
    assert search_page.is_menu_elements_present() is True

    search_page.perform_search(phrase)
    assert phrase in result_page.get_title()
    assert phrase in result_page.get_url()
    assert result_page.get_suggested_option_text() == valid_suggested_phrase

    result_page.open_suggested_option()
    assert result_page.get_textarea_text() == valid_suggested_phrase
    assert valid_suggested_phrase in result_page.driver.current_url
    assert valid_suggested_phrase in result_page.get_result_title().lower()

    result_page.click_images()
    assert images_result_page.is_images_button_selected() is True
