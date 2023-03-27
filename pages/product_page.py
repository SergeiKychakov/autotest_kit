import time
from .base_page import BasePage
from .locators import ProductPageLocators

class PageObject(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
        button.click()

    def count_in_allert_example(self):
        assert self.solve_quiz_and_get_code(), "CODE NOT FIND"
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "SUCCESS MESSAGE IS PRESENTED, BUT SHOULD NOT BE"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "SUCCESS MESSAGE IS PRESENTED, BUT SHOULD NOT BE"

    
    def checking(self):
        assert self.browser.find_element_by_tag_name("strong").text == \
            self.browser.find_element(*ProductPageLocators.BOOK_NAME).\
                text, "NOT RIGHT"
        # assert self.browser.find_element_by_tag_name("strong").text \
        # == self.browser.find_element(*ProductPageLocators.PRICE), "NOT RIGHT"

       