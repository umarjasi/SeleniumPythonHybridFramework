from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage


class AccountSuccessPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    account_creation_msg_xpath = "//div[@id='content']/h1"

    def retrieve_account_creation_msg(self):
        return self.retrieve_element_text("account_creation_msg_xpath",self.account_creation_msg_xpath)
