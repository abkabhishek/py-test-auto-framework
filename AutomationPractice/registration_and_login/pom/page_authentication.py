from selenium.webdriver.support.select import Select

from AutomationPractice.registration_and_login.pom.base import BasePage
from AutomationPractice.registration_and_login.pom.locators import Locators


class AuthenticationPage(BasePage):
    """ Authentication Page Class
        It contains multiple sub section: Login, Create Account and Personal Info section as class composition
    """

    def __init__(self, driver):
        BasePage.__init__(self, driver)

        self.login_section = LoginSection(self)
        self.create_account_section = CreateAccountSection(self)
        self.personal_info_section = PersonalInfoSection(self)


class LoginSection:
    """ Login section """
    driver = None

    def __init__(self, page):
        self.page = page

        # Below is creating class attribute for each locator in Locator class as one Element object and one locator_* string
        for k, v in Locators.Authentication_login.items():
            setattr(self, k, self.page.com.element(v))
            setattr(self, "elem_ " + k, v)

    def input_email_address(self, email):
        self.textbox_email().send_keys(email)

    def input_password(self, password):
        self.textbox_password().send_keys(password)

    def click_sign_in_button(self):
        self.button_sign_in().click()

    def perform_login(self, email, password, wait_for_next_page_load=True):
        self.input_email_address(email)
        self.input_password(password)
        self.click_sign_in_button()
        if wait_for_next_page_load:
            self.page.wait_for_page_load("myaccountpage")

    def get_error_list(self):
        errors = [x.text for x in self.list_error_items(find_all=True)]
        return errors

    def is_login_error_occured(self):
        return (len(self.get_error_list()) > 0)


class CreateAccountSection:
    """ Create Account Section """

    def __init__(self, page):
        self.page = page

        # Below is creating class attribute for each locator in Locator class as one Element object and one locator_* string
        for k, v in Locators.Authentication_create_account.items():
            setattr(self, k, self.page.com.element(v))
            setattr(self, "elem_ " + k, v)

    def input_email_address(self, email):
        self.textbox_email().send_keys(email)

    def click_button_create_account(self, wait_for_next_page_load=True):
        self.button_create_account().click()
        if wait_for_next_page_load:
            self.page.wait_for_page_load("personalinfopage")


class PersonalInfoSection:
    """ Personal Info fields section"""

    def __init__(self, page):
        self.page = page

        # Below is creating class attribute for each locator in Locator class as one Element object and one locator_* string
        for k, v in Locators.Authentication_personal_info.items():
            setattr(self, k, self.page.com.element(v))
            setattr(self, "elem_ " + k, v)

    def get_section_heading(self):
        return self.subheadings().text

    def input_personal_info(self, fields_values):
        if "title" in fields_values:
            if fields_values["title"] == "mrs":
                self.field_option_title_Mrs().click()
            else:
                self.field_option_title_Mr().click()

        if "first_name" in fields_values:
            self.field_textbox_first_name().send_keys(fields_values["first_name"])
            # self.field_textbox_address_firstname().send_keys(fields_values["first_name"])

        if "last_name" in fields_values:
            self.field_textbox_last_name().send_keys(fields_values["last_name"])
            # self.field_textbox_address_lastname().send_keys(fields_values["last_name"])

        if "email" not in fields_values:
            if self.field_textbox_email().get_attribute('value'):
                self.field_textbox_email().clear()

        if "password" in fields_values:
            self.field_textbox_password().send_keys(fields_values["password"])

        if "dob_date" in fields_values:
            Select(self.field_select_dob_day()).select_by_value(str(fields_values["dob_date"]))

        if "dob_month" in fields_values:
            Select(self.field_select_dob_month()).select_by_value(str(fields_values["dob_month"]))

        if "dob_year" in fields_values:
            Select(self.field_select_dob_year()).select_by_value(str(fields_values["dob_year"]))

        if "company" in fields_values:
            self.field_textbox_address_company().send_keys(fields_values["company"])

        if "address1" in fields_values:
            self.field_textbox_address_address1().send_keys(fields_values["address1"])

        if "address2" in fields_values:
            self.field_textbox_address_address2().send_keys(fields_values["address2"])

        if "city" in fields_values:
            self.field_textbox_address_city().send_keys(fields_values["city"])

        if "state_index" in fields_values:
            Select(self.field_select_address_state()).select_by_value(str(fields_values["state_index"]))

        if "zipcode" in fields_values:
            self.field_textbox_address_postcode().send_keys(fields_values["zipcode"])

        if "additional_info" in fields_values:
            self.field_textbox_address_additionalinfo().send_keys(fields_values["additional_info"])

        if "home_phone" in fields_values:
            self.field_textbox_address_phone().send_keys(fields_values["home_phone"])

        if "mobile_phone" in fields_values:
            self.field_textbox_address_mobile().send_keys(fields_values["mobile_phone"])

        if "address_alias" in fields_values:
            el_ad_alias = self.field_textbox_address_alias()
            el_ad_alias.clear()
            el_ad_alias.send_keys(fields_values["address_alias"])
        else:
            el_ad_alias = self.field_textbox_address_alias()
            el_ad_alias.clear()

    def click_button_register(self, wait_for_next_page_load=True):
        self.button_register().click()
        if wait_for_next_page_load:
            self.page.wait_for_page_load("myaccountpage")

    def get_error_list(self):
        errors = [x.text for x in self.list_error_items(find_all=True)]
        return errors

    def is_login_error_occured(self):
        return (len(self.get_error_list()) > 0)
