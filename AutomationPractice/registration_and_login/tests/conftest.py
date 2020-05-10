"""
Shared Fixtures
"""

import json
import os
import pytest
import selenium.webdriver

from AutomationPractice.registration_and_login.pom.page_home import HomePage
from AutomationPractice.registration_and_login.pom.page_authentication import AuthenticationPage
from AutomationPractice.registration_and_login.pom.page_myaccount import MyaccountPage
from core.browser import Browser

dir_path = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture
def config(scope='session'):
    # Read the file
    with open(os.path.join(dir_path, 'config_test.json')) as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['firefox', 'chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture
def app(config):
    # get Web Driver
    b = Browser.get_driver({"browser": config['browser'], "environment": config['environment'],"headless":config["headless"]})

    # Make its calls wait for elements to appear
    if config['environment']=="remote":
        b.implicitly_wait(config['implicit_wait']+30)
    else:
        b.implicitly_wait(config['implicit_wait'])

    app = App(b, config['base_url'])

    yield app

    b.quit()
    del app


class App:

    def __init__(self, driver, base_url):
        self.home_page = HomePage(driver, base_url)
        self.authentication_page = AuthenticationPage(driver)
        self.myaccount_page = MyaccountPage(driver)
