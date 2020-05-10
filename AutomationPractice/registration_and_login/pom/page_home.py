from AutomationPractice.registration_and_login.pom.base import BasePage
from AutomationPractice.registration_and_login.pom.locators import Locators


class HomePage(BasePage):
    """ Home Page Class """

    def __init__(self, driver, base_url=None):
        BasePage.__init__(self, driver)
        self.base_url = base_url

        # Below is creating class attribute for each locator in Locator class as one Element object and one locator_* string
        for k, v in Locators.Home.items():
            setattr(self, k, self.com.element(v))
            setattr(self, "elem_ " + k, v)

    def open_homepage(self):
        self.driver.get(self.base_url)
        self.wait_for_page_load("homepage")

    def click_sign_in(self):
        self.link_sign_in().click()
        self.wait_for_page_load("loginpage")

    def click_sign_out(self):
        self.link_sign_out().click()
