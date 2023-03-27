from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import link

class LoginPage(BasePage):
    def register_new_user(email, password):
        pass

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert link in self.browser.current_url, \
            "Некорректный адрес страницы" # сообщение об ошибке

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM)\
             == True, "Login form is invalid" # сообщение об ошибке

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM)\
             == True, "Registration form is invalid" # сообщение об ошибке