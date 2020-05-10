from faker import Faker
import os
from pprint import pprint
from sys import stdout as console

dir_path = os.path.dirname(os.path.realpath(__file__))


class TestDataProvider:
    """This is Test Data Provider class to supply test data after generating it as per requirement to test functions and saving created account in a csv file for later use."""
    email_template = "autopracuser{}@mailnesia.com"
    currentCount = None




    @classmethod
    def save_created_account(cls, email, password):
        """
        To Save created account details for later use and not to generate same email account for new registration.
        New created account should be saved through this
        """
        with open(os.path.join(dir_path, "created_accounts.csv"), "a+") as fl:
            fl.write("{}, {}\n".format(email, password))
        console.write("====== Created User is Saved =======")

    @classmethod
    def get_created_account(cls, get_all=False):
        """ To get account credentials for existing created account """
        try:
            with open(os.path.join(dir_path, "created_accounts.csv"), "r") as fl:
                if get_all:
                    account = [[account.rstrip("\n").split(", ")] for account in fl.readlines()]
                else:
                    account = fl.readline().rstrip("\n").split(", ")
        except FileNotFoundError as e:
            return 0, "No account is available"
        return account

    @classmethod
    def generate_user_reg_data(cls, count=1, without_fields=None, only_required_fields=False,save_user=False):
        """
        To Generate Personal Information Fields data for new account registration
        """
        faker = Faker()
        user_reg_data_list = []

        for i in range(count):
            user_reg_data = {}

            user_reg_data["first_name"], user_reg_data["last_name"] = faker.first_name(), faker.last_name()
            user_reg_data["email"] = cls.generate_email()
            user_reg_data["password"] = "autoprac1234"
            if save_user:
                cls.save_created_account(user_reg_data["email"],user_reg_data["password"])
            address = faker.address()
            first_address, second_address = address.split("\n")
            # _,state,zipcode = second_address.split()
            user_reg_data["address1"] = first_address

            user_reg_data["city"] = faker.city()
            user_reg_data["state_index"] = faker.random_int(1, 53)
            user_reg_data["zipcode"] = faker.zipcode()

            user_reg_data["mobile_phone"] = 1111111112
            user_reg_data["address_alias"] = str(user_reg_data["state_index"]) + str(user_reg_data["zipcode"])

            if only_required_fields == False:
                title = faker.boolean()
                if title:
                    user_reg_data["title"] = "mrs"
                else:
                    user_reg_data["title"] = "mr"
                dob = str(faker.date_of_birth())
                dob_year, dob_month, dob_date = dob.split("-")
                user_reg_data["dob_year"], user_reg_data["dob_month"], user_reg_data["dob_date"] = int(dob_year), int(
                    dob_month), int(dob_date)
                user_reg_data["company"] = faker.company()
                user_reg_data["address2"] = second_address
                user_reg_data["home_phone"] = 1111111111
                user_reg_data["additional_info"] = faker.text()

            if without_fields:
                for item in without_fields:
                    del user_reg_data[item]
            user_reg_data_list.append(user_reg_data)

        return user_reg_data_list

    @classmethod
    def generate_email(cls):
        """To Generated new Email for new account creation as per saved account details """
        return cls.email_template.format(cls.get_number_of_accounts() + 1)

    @classmethod
    def get_number_of_accounts(cls):
        accounts = cls.get_created_account(get_all=True)
        total_accounts = len(accounts)
        TestDataProvider.currentCount = total_accounts
        return total_accounts


    @classmethod
    def get_creds_list_neg_combo1(cls):
        """
        For Login Tests,
        It provide negative test data with expected error.
        """
        user_creds_list = [({"username": "autopracuser1@mailnsia.com", "password": "autoprac1234"},
                            "Login - My Store",
                            1, ["Authentication failed."]),
                           ({"username": "autopracuser1@mailnesia.com", "password": "dautoprac1234"},
                            "Login - My Store",
                            1, ["Authentication failed."]),
                           ({"username": "autopracuser1@mailnsia.com", "password": "dautoprac1234"},
                            "Login - My Store",
                            1, ["Authentication failed."]),
                           ({"username": "", "password": ""},
                            "Login - My Store",
                            1, ["An email address required."]),
                           ({"username": "asdfj@asdkjfh.com", "password": ""},
                            "Login - My Store",
                            1, ["Password is required."]),
                           ({"username": "", "password": "asdfasdf"},
                            "Login - My Store",
                            1, ["An email address required."])
                           ]
        return user_creds_list

    @classmethod
    def get_user_reg_data_list_with_errors(cls):
        """
        For Registration Tests.
        This test function provides negative test data as required field.
        One row of data is missing with one required field at a time and their expected error.
        """
        required_fields_errors = {
            "first_name": "firstname is required.",
            "last_name": "lastname is required.",
            "email": "email is required.",
            "password": "passwd is required.",
            "address1": "address1 is required.",
            "city": "city is required.",
            "state_index": "This country requires you to choose a State.",
            "zipcode": "The Zip/Postal code you've entered is invalid. It must follow this format: 00000",
            "mobile_phone": "You must register at least one phone number.",
            "address_alias": "alias is required."
        }

        generated_data = []
        for k, v in required_fields_errors.items():
            data1 = (cls.generate_user_reg_data(without_fields=[k], only_required_fields=True)[0],
                     [v])
            data1[0]["email_for_create_account_page"] = cls.generate_email()

            generated_data.append(data1)
        return generated_data
