import pytest
from AutomationPractice.registration_and_login.testdata.test_data_provider import TestDataProvider


class TestLogin:

    @pytest.mark.positive
    def test_open_homepage(self,app):
        app.home_page.open_homepage()
        assert("My Store" == app.home_page.get_title())


    @pytest.mark.positive
    @pytest.mark.parametrize("user_creds,page_title",
                             [({"username": "autopracuser1@mailnesia.com", "password": "autoprac1234"},
                               "My account - My Store")])
    def test_login_success(self, app, user_creds, page_title):
        app.home_page.open_homepage()
        app.home_page.click_sign_in()
        app.authentication_page.login_section.perform_login(user_creds["username"], user_creds["password"])
        assert (page_title == app.authentication_page.get_title())




    @pytest.mark.negative
    @pytest.mark.parametrize("user_creds,page_title,error_count,expected_errors",
                             TestDataProvider.get_creds_list_neg_combo1())
    def test_login_failure_invalid_creds(self, app, user_creds, page_title, error_count, expected_errors):
        app.home_page.open_homepage()
        app.home_page.click_sign_in()
        app.authentication_page.login_section.perform_login(user_creds["username"], user_creds["password"],
                                                            wait_for_next_page_load=False)
        errors = app.authentication_page.login_section.get_error_list()
        pytest.assume(error_count == len(errors))
        for i in range(error_count):
            pytest.assume(expected_errors[i] == errors[i])
        pytest.assume(page_title == app.authentication_page.get_title())
