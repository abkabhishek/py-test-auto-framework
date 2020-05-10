"""
This is base page to handle common elements,methods across the pages.
"""

from selenium.common.exceptions import ElementNotVisibleException

from core.com import Com
from AutomationPractice.registration_and_login.pom.locators import Locators


class BasePage(object):
    """ This is Base Page class. For all common properties and methods. All page classes inherit this class."""
    driver = None
    Locators = Locators

    def __init__(self, driver):
        BasePage.driver = driver
        self.com = Com(driver)

    def open_url(self, url):
        self.driver.get(url)

    def close(self):
        BasePage.driver.close()

    def quit(self):
        BasePage.driver.quit()

    def get_title(self):
        return self.driver.title

    def get_page_h1_heading_text(self):
        return self.com.findElement(self.Locators.Authentication_personal_info['heading']).text

    def wait_for_page_load(self, page_name):
        try:
            if page_name == "homepage":
                self.com.wait.wait_for_element_visible(self.Locators.Home["link_sign_in"])
            elif page_name == "loginpage" or page_name == "createaccount":
                self.com.wait.wait_for_element_visible(self.Locators.Authentication_create_account["subheading"])
            elif page_name == "personalinfopage":
                self.com.wait.wait_for_element_with_text_present(
                    self.Locators.Authentication_personal_info['subheadings'], "YOUR PERSONAL INFORMATION")
            elif page_name == "myaccountpage":
                self.com.wait.wait_for_element_visible(self.Locators.Myaccount["link_account"])
            else:
                raise Exception("Incorrect Page Name passed")
        except ElementNotVisibleException as e:
            print(e)
            raise Exception("Page {} is unable to load".format(page_name))
