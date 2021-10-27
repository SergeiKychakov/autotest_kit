from .base_page import BasePage

class PageObject(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
        button.click()

    def count_in_allert_example(self):
        assert self.solve_quiz_and_get_code(), "CODE NOT FIND"


    #def checking(self):
        #book_name = self.browser.find_element(*CheckBasketLocators.BOOK_NAME).text
        #price = self.browser.find_element(*CheckBasketLocators.PRICE).text
        #button = self.browser.find_element_by_class_name("btn.btn-default")
        #button.click()
        #assert book_name == self.browser.find_element(*CheckBasketLocators.BOOK_NAME), "NOT RIGHT"
        #assert price == self.browser.find_element(*CheckBasketLocators.PRICE), "NOT RIGHT"

       