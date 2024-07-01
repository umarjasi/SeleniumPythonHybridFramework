from PageObjects.AccountPage import AccountPage
from PageObjects.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    email_address_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    warning_message_xpath = "//div[@class='alert alert-danger alert-dismissible']"

    def enter_email_id(self,email_address_text):
        self.type_into_element(email_address_text,"email_address_id",self.email_address_id)

    def enter_password(self,password_text):
        self.type_into_element(password_text, "password_field_id",self.password_field_id)

    def click_login(self):
        self.element_click("login_button_xpath",self.login_button_xpath)
        return AccountPage(self.driver)

    def login_to_application(self, email_address_text, password_text):
        self.enter_email_id(email_address_text)
        self.enter_password(password_text)
        return self.click_login()

    def retrieve_warning_message(self):
        return self.retrieve_element_text("warning_message_xpath",self.warning_message_xpath)


