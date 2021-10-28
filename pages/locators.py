from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR,"#login-username"), \
    (By.CSS_SELECTOR, "#login-password")
    REGISTER_FORM = (By.CSS_SELECTOR, "#id_registration-email"), \
    (By.CSS_SELECTOR, "#id_registration-password"), \
    (By.CSS_SELECTOR, "#id_registration-password2")

class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CLASS_NAME, ".alert.alert-safe.alert-noicon.alert-sucess.fade.in")
    # BOOK_NAME = (By.TAG_NAME, "h1")
    # PRICE = (By.CSS.SELECTOR, ".price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")