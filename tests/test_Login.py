from datetime import datetime
import pytest
from PageObjects.HomePage import HomePage
from tests.BaseTest import BaseTest
from utilities import ExcelReader


class TestLogin(BaseTest):
    @pytest.mark.parametrize("email_address,password",ExcelReader.get_data_from_excel("ExcelFiles/TutorialsNinjas.xlsx", "LoginTest"))
    def test_login_with_valid_credentials(self,email_address,password):
        home_page = HomePage(self.driver)
        loginpage = home_page.navigate_to_login_page()
        accountpage =loginpage.login_to_application(email_address,password)
        assert accountpage.display_status_of_edit_account_information()

    def test_login_with_invalid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        loginpage = home_page.navigate_to_login_page()
        loginpage.login_to_application(self.generate_email_time_stamp(),"syn12345")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert loginpage.retrieve_warning_message().__contains__(expected_warning_message)

    def test_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        loginpage = home_page.navigate_to_login_page()
        loginpage.login_to_application("umarfaru01@gmail.com", "syn12345987")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert loginpage.retrieve_warning_message().__contains__(expected_warning_message)

    def test_login_without_entering_credentials(self):
        home_page = HomePage(self.driver)
        loginpage = home_page.navigate_to_login_page()
        loginpage.login_to_application("", "")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert loginpage.retrieve_warning_message().__contains__(expected_warning_message)

    def generate_email_time_stamp(self):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return "arun"+timestamp+"@gmail.com"
