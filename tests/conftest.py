import pytest
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def config(scope='session'):
    with open('data/config.json') as config_file:
        config = json.load(config_file)

    assert config['browser'] in ['Chrome', 'Headless Chrome']
    assert config['url'] is not "" or None

    return config


@pytest.fixture
def browser(config):
    if config['browser'] == 'Chrome':
        chrome_options = Options()
        [chrome_options.add_argument(option) for option in config["chromeOptions"]]
        driver = webdriver.Chrome(options=chrome_options)
    elif config['browser'] == 'Headless Chrome':
        chrome_options = Options()
        [chrome_options.add_argument(option) for option in config["chromeOptions"]]
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    driver.delete_all_cookies()

    yield driver

    driver.close()
    driver.quit()
