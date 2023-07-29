from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.poll = 2
        self.timeout = 10

    def navigate_to(self, url):
        self.driver.get(url)

    def click(self, element):
        self.wait_element_clickeable(element)
        element.click()

    def send_keys(self, element, keys):
        self.wait_element_visibility(element)
        element.send_keys(keys)

    def wait_element_visibility(self, element):
        wait = WebDriverWait(self.driver, timeout=self.timeout, poll_frequency=self.poll)
        wait.until(ec.visibility_of(element))

    def wait_element_clickeable(self, element):
        self.wait_element_visibility(element)
        wait = WebDriverWait(self.driver, timeout=self.timeout, poll_frequency=self.poll)
        wait.until(ec.element_to_be_clickable(element))
    
    def get_title(self):
        return self.driver.title
    
    def get_url(self):
        return self.driver.current_url

