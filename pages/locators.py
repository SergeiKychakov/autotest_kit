from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

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

class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")