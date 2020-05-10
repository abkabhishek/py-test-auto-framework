import time

import pytest
from AutomationPractice.registration_and_login.testdata.test_data_provider import TestDataProvider


class TestRegistration:


    @pytest.mark.positive
    @pytest.mark.parametrize("new_user_data",
                             TestDataProvider.generate_user_reg_data(save_user=True))
    def test_registration_success_scenario(self, app, new_user_data):
        # TestDataProvider.save_created_account(new_user_data["email"], new_user_data["password"])
        app.home_page.open_homepage()
        app.home_page.click_sign_in()
        app.authentication_page.create_account_section.input_email_address(new_user_data["email"])
        app.authentication_page.create_account_section.click_button_create_account()
        actual = app.authentication_page.get_page_h1_heading_text()
        pytest.assume("CREATE AN ACCOUNT" == actual, "Actual:{} ,Expected: {}".format(actual, "CREATE AN ACCOUNT"))
        actual = app.authentication_page.personal_info_section.get_section_heading()
        pytest.assume("YOUR PERSONAL INFORMATION" == actual,
                      "Actual:{} ,Expected: {}".format(actual, "YOUR PERSONAL INFORMATION"))

        app.authentication_page.personal_info_section.input_personal_info(new_user_data)
        app.authentication_page.personal_info_section.click_button_register()
        title = app.authentication_page.get_title()
        expected_title = "My account - My Store"
        pytest.assume(title == expected_title, "Actual:{} ,Expected: {}".format(title, expected_title))
        full_name = app.myaccount_page.get_logged_in_full_name()
        expected_full_name = new_user_data["first_name"] + " " + new_user_data["last_name"]
        pytest.assume(full_name == expected_full_name.lower(),
                      "Actual:{} ,Expected: {}".format(full_name, expected_full_name))

    @pytest.mark.positive
    @pytest.mark.parametrize("new_user_data",
                             TestDataProvider.generate_user_reg_data(only_required_fields=True,save_user=True))
    def test_registration_success_scenario_only_required_fields(self, app, new_user_data):
        # TestDataProvider.save_created_account(new_user_data["email"], new_user_data["password"])
        app.home_page.open_homepage()
        app.home_page.click_sign_in()
        app.authentication_page.create_account_section.input_email_address(new_user_data["email"])
        app.authentication_page.create_account_section.click_button_create_account()
        actual = app.authentication_page.get_page_h1_heading_text()
        pytest.assume("CREATE AN ACCOUNT" == actual, "Actual:{} ,Expected: {}".format(actual, "CREATE AN ACCOUNT"))
        actual = app.authentication_page.personal_info_section.get_section_heading()
        pytest.assume("YOUR PERSONAL INFORMATION" == actual,
                      "Actual:{} ,Expected: {}".format(actual, "YOUR PERSONAL INFORMATION"))

        app.authentication_page.personal_info_section.input_personal_info(new_user_data)
        app.authentication_page.personal_info_section.click_button_register()
        title = app.authentication_page.get_title()
        expected_title = "My account - My Store"
        pytest.assume(title == expected_title, "Actual:{} ,Expected: {}".format(title, expected_title))
        full_name = app.myaccount_page.get_logged_in_full_name()
        expected_full_name = new_user_data["first_name"] + " " + new_user_data["last_name"]
        pytest.assume(full_name == expected_full_name.lower(),
                      "Actual:{} ,Expected: {}".format(full_name, expected_full_name))

    @pytest.mark.negative
    @pytest.mark.parametrize("new_user_data,errors",
                             TestDataProvider.get_user_reg_data_list_with_errors())
    def test_registration_personal_info_page_all_negative_scenarios_without_required_field(self, app, new_user_data,
                                                                                           errors):
        app.home_page.open_homepage()
        app.home_page.click_sign_in()
        app.authentication_page.create_account_section.input_email_address(
            new_user_data["email_for_create_account_page"])
        app.authentication_page.create_account_section.click_button_create_account()
        app.authentication_page.personal_info_section.input_personal_info(new_user_data)
        app.authentication_page.personal_info_section.click_button_register(wait_for_next_page_load=False)
        actual_errors = app.authentication_page.personal_info_section.get_error_list()
        pytest.assume(len(actual_errors) == len(errors),
                      "Actual:{} ,Expected: {}".format(len(actual_errors), len(errors)))
        for i in range(len(errors)):
            pytest.assume(actual_errors[i] == errors[i], "Actual:{} ,Expected: {}".format(actual_errors[i], errors[i]))
