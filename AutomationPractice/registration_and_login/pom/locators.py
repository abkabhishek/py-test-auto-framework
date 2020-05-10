class Locators:
    Home = {
        'link_sign_in': 'css|a.login',
        'link_sign_out': 'css|a.logout'
    }

    Authentication_create_account = {
        'heading': 'tagname|h1',
        'subheading': 'css|form#create-account_form h3',
        'textbox_email': 'id|email_create',
        'button_create_account': 'id|SubmitCreate',
        'list_error_items': 'css|#create_account_error>ol>li'
    }

    Authentication_login = {
        'heading': 'tagname|h1',
        'subheadings': 'css|form#login_form h3',
        'textbox_email': 'id|email',
        'textbox_password': 'id|passwd',
        'button_sign_in': 'id|SubmitLogin',
        'list_error_items': 'css|div.center_column> :nth-child(2)>ol>li'
    }

    Authentication_personal_info = {
        'heading': 'tagname|h1',
        'subheadings': 'tagname|h3',
        'div_account_creation': 'css|div.account_creation',
        'field_option_title_Mr': 'id|uniform-id_gender1',
        'field_option_title_Mrs': 'id|uniform-id_gender2',
        'field_textbox_first_name': 'id|customer_firstname',
        'field_textbox_last_name': 'id|customer_lastname',
        'field_textbox_email': 'id|email',
        'field_textbox_password': 'id|passwd',
        'field_select_dob_day': 'id|days',
        'field_select_dob_month': 'id|months',
        'field_select_dob_year': 'id|years',
        'field_checkbox_newsletter': 'id|uniform-newsletter',
        'field_checkbox_offers': 'id|uniform-optin',
        'field_textbox_address_firstname': 'id|firstname',
        'field_textbox_address_lastname': 'id|lastname',
        'field_textbox_address_company': 'id|company',
        'field_textbox_address_address1': 'id|address1',
        'field_textbox_address_address2': 'id|address2',
        'field_textbox_address_city': 'id|city',
        'field_select_address_state': 'id|id_state',
        'field_textbox_address_postcode': 'id|postcode',
        'field_select_address_country': 'id|id_country',
        'field_textbox_address_additionalinfo': 'id|other',
        'field_textbox_address_phone': 'id|phone',
        'field_textbox_address_mobile': 'id|phone_mobile',
        'field_textbox_address_alias': 'id|alias',
        'field_textbox_tax_idno': 'id|dni',
        'list_error_items': 'css|.alert-danger>ol>li',
        'button_register': 'id|submitAccount'
    }

    Myaccount = {
        'heading': 'tagname|h1',
        'link_account': 'css|a.account'
    }
