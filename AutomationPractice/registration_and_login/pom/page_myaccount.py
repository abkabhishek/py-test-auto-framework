from AutomationPractice.registration_and_login.pom.base import BasePage
from AutomationPractice.registration_and_login.pom.locators import Locators


class MyaccountPage(BasePage):
    """ My Account Page Class """

    def __init__(self, driver):
        BasePage.__init__(self, driver)

        # Below is creating class attribute for each locator in Locator class as one Element object and one locator_* string
        for k, v in Locators.Myaccount.items():
            setattr(self, k, self.com.element(v))
            setattr(self, "elem_ " + k, v)

    def get_logged_in_full_name(self):
        return self.link_account().text.lower()
