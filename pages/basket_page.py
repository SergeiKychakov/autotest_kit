from .base_page import BasePage
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def check_empty_basket(self):
        assert self.find_element(By.LINK_TEXT, " Your basket is empty. "), "BASKET NOT EMPTY"

    def check_not_empty_basket(self):
        assert not self.find_element(By.LINK_TEXT, " Your basket is empty. "), "BASKET EMPTY"
            


    
