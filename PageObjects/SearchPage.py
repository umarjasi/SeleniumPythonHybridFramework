from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    valid_hp_product_link_text = "HP LP3065"
    no_product_message_xpath = "//p[contains(text(),'There is no product that matches the search criter')]"

    def display_status_of_hp_product(self):
        return self.check_display_status_of_element("valid_hp_product_link_text",self.valid_hp_product_link_text)

    def retrieving_no_product_message(self):
        return self.retrieve_element_text("no_product_message_xpath",self.no_product_message_xpath)
