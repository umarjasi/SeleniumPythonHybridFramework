from selenium.webdriver.common.by import By

from PageObjects.AccountSuccessPage import AccountSuccessPage
from PageObjects.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    first_name_field_id = "input-firstname"
    last_name_field_id = "input-lastname"
    email_field_id = "input-email"
    telephone_no_id = "input-telephone"
    password_no_id = "input-password"
    confirm_pwd_id = "input-confirm"
    agree_field_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    yes_radio_button_xpath = "//label[normalize-space()='Yes']"
    warning_message_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    privacy_policy_warning_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    firstname_warning_xpath = "//div[contains(text(),'First Name must be between 1 and 32 characters!')]"
    lastname_warning_xpath = "//div[contains(text(),'Last Name must be between 1 and 32 characters!')]"
    email_warning_xpath = "//div[contains(text(),'E-Mail Address does not appear to be valid!')]"
    telephone_warning_xpath = "//div[contains(text(),'Telephone must be between 3 and 32 characters!')]"
    password_warning_xpath = "//div[contains(text(),'Password must be between 4 and 20 characters!')]"


    def enter_first_name(self,first_name_text):
        self.type_into_element(first_name_text,"first_name_field_id",self.first_name_field_id)


    def enter_last_name(self,last_name_text):
        self.type_into_element(last_name_text, "last_name_field_id",self.last_name_field_id)


    def enter_email(self,email_text):
        self.type_into_element(email_text,"email_field_id", self.email_field_id)


    def enter_telephone(self,telephone_no):
        self.type_into_element(telephone_no,"telephone_no_id", self.telephone_no_id)

    def enter_password(self,password):
        self.type_into_element(password,"password_no_id", self.password_no_id)


    def confirm_password(self,confirmpwd):
        self.type_into_element(confirmpwd,"confirm_pwd_id", self.confirm_pwd_id)


    def select_agree_checkbox_field(self):
        self.element_click("agree_field_name",self.agree_field_name)


    def click_on_continue_button(self):
        self.element_click("continue_button_xpath",self.continue_button_xpath)
        return AccountSuccessPage(self.driver)

    def select_yes_radio_btn(self):
        self.element_click("yes_radio_button_xpath",self.yes_radio_button_xpath)

    def register_an_account(self, first_name_text, last_name_text, email_text, telephone_no, password,
                            confirmpwd, yes_or_no, privacy_policy):
        self.enter_first_name(first_name_text)
        self.enter_last_name(last_name_text)
        self.enter_email(email_text)
        self.enter_telephone(telephone_no)
        self.enter_password(password)
        self.confirm_password(confirmpwd)
        if yes_or_no.__eq__("yes"):
            self.select_yes_radio_btn()
        if privacy_policy.__eq__("select"):
            self.select_agree_checkbox_field()
        return self.click_on_continue_button()

    def email_warning(self):
        return self.retrieve_element_text("warning_message_xpath",self.warning_message_xpath)

    def privacy_polcy_warning(self):
        return self.retrieve_element_text("warning_message_xpath",self.warning_message_xpath)

    def first_name_warning(self):
        return self.retrieve_element_text("firstname_warning_xpath",self.firstname_warning_xpath)

    def last_name_warning(self):
        return self.retrieve_element_text("lastname_warning_xpath",self.lastname_warning_xpath)

    def retrieve_email_warning(self):
        return self.retrieve_element_text("email_warning_xpath",self.email_warning_xpath)

    def telephone_warning(self):
        return self.retrieve_element_text("telephone_warning_xpath",self.telephone_warning_xpath)

    def password_warning(self):
        return self.retrieve_element_text("password_warning_xpath",self.password_warning_xpath)







