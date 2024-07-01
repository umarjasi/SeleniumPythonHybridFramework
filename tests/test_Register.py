import time
import pytest
from PageObjects.AccountSuccessPage import AccountSuccessPage
from PageObjects.HomePage import HomePage
from PageObjects.RegisterPage import RegisterPage
from tests.BaseTest import BaseTest
from utilities import ExcelReader


class TestRegister(BaseTest):
    def test_create_account_with_mandatory_fiels(self):
        home_page = HomePage(self.driver)
        registerpage = home_page.navigate_to_register_page()
        accountsuccess = registerpage.register_an_account(
            ExcelReader.get_cell_data("ExcelFiles/TutorialsNinjas.xlsx","RegisterTest",2,1),
            ExcelReader.get_cell_data("ExcelFiles/TutorialsNinjas.xlsx","RegisterTest",2,2),self.generate_email_time_stamp(),"1234567890","12345","12345","no","select")
        expected_text = "Your Account Has Been Created!"
        assert accountsuccess.retrieve_account_creation_msg().__eq__(expected_text)

    def test_create_account_by_providing_all_fields(self):
        home_page = HomePage(self.driver)
        registerpage = home_page.navigate_to_register_page()
        accountsuccess = registerpage.register_an_account("umar", "farook", self.generate_email_time_stamp(),
                                                          "1234567890", "12345", "12345", "yes", "select")
        expected_text = "Your Account Has Been Created!"
        assert accountsuccess.retrieve_account_creation_msg().__eq__(expected_text)

    def test_create_account_with_existing_email(self):
        home_page = HomePage(self.driver)
        registerpage = home_page.navigate_to_register_page()
        registerpage.register_an_account("umar", "farook", "umarfaru01@gmail.com",
                                                          "1234567890", "12345", "12345", "yes", "select")

        expected_warning_message = "Warning: E-Mail Address is already registered!"
        assert registerpage.email_warning().__contains__(expected_warning_message)

    def test_without_providing_all_fields(self):
        home_page = HomePage(self.driver)
        registerpage = home_page.navigate_to_register_page()
        registerpage.register_an_account("", "", "",
                                         "", "", "", "no", "no")
        expected_privacy_policy = "Warning: You must agree to the Privacy Policy!"
        assert registerpage.privacy_polcy_warning().__contains__(expected_privacy_policy)
        expected_first_name_warning = "First Name must be between 1 and 32 characters!"
        assert registerpage.first_name_warning().__eq__(expected_first_name_warning)
        expected_last_name_warning = "Last Name must be between 1 and 32 characters!"
        assert registerpage.last_name_warning().__eq__(expected_last_name_warning)
        expected_email_warning = "E-Mail Address does not appear to be valid!"
        assert registerpage.retrieve_email_warning().__eq__(expected_email_warning)
        expected_telephone_warning = "Telephone must be between 3 and 32 characters!"
        assert registerpage.telephone_warning().__eq__(expected_telephone_warning)
        expected_password_warning = "Password must be between 4 and 20 characters!"
        assert registerpage.password_warning().__eq__(expected_password_warning)

    def generate_email_time_stamp(self):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        timestamp = timestamp.replace('-', '_').replace(' ', '_').replace(':', '_')
        return "arun" + timestamp + "@gmail.com"