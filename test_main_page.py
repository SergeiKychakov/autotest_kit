from .pages.main_page import MainPage
from .pages.locators import link
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)  # инициализируем Page Object, 
    # передаем в конструктор экземпляр драйвера и url адрес 
    page.open() # открываем страницу
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)  # инициализируем Page Object, 
    # передаем в конструктор экземпляр драйвера и url адрес 
    page.open() # открываем страницу
    page.go_to_basket() # заходим в корзину
    page.check_empty_basket()



def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

