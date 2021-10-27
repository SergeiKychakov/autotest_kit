from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR,"#login-username"), \
    (By.CSS_SELECTOR, "#login-password")
    REGISTER_FORM = (By.CSS_SELECTOR, "#id_registration-email"), \
    (By.CSS_SELECTOR, "#id_registration-password"), \
    (By.CSS_SELECTOR, "#id_registration-password2")

#class CheckBasketLocators():
    #BOOK_NAME = (By.CSS.SELECTOR,)
    #PRICE = (By.CSS.SELECTOR,)

