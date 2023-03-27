import pytest
import time
from .pages.product_page import PageObject
from .pages.basket_page import BasketPage

@pytest.mark.parametrize('promo_offer', ["1", "2", "3", "4", "5", "6", "7", "8", "9"])
@pytest.mark.parametrize('link', ["okay_link", pytest.param("bugged_link", marks=pytest.mark.xfail), "okay_link"])

class TestUserAddToBasketFromProductPage:

    def test_guest_cant_see_success_message(browser, link):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = PageObject(browser, link)
        page.open()
        time.sleep(1)
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(browser, promo_offer):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
        page = PageObject(browser, link)  # инициализируем Page Object, 
        # передаем в конструктор экземпляр драйвера и url адрес 
        page.open() # открываем страницу
        page.add_to_basket() # добавляем книгу в корзину
        page.count_in_allert_example() # считаем значание в алерте и нажимаем ОК
        page.should_not_be_success_message()
        page.checking() # проверка сообщения об успешном добавление в корзину

@pytest.mark.new # запуск pytest -s -m "new" test_product_page.py
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.new # запуск pytest -s -m "new" test_product_page.py
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.new # запуск pytest -s -m "new" test_product_page.py
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.go_to_basket() # заходим в корзину
    page.check_empty_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = PageObject(browser, link)
    page.open()
    page.add_to_basket()
    time.sleep(1)
    page.should_not_be_success_message()
   
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = PageObject(browser, link)
    page.open()
    page.add_to_basket()
    time.sleep(1)
    page.should_dissapear_of_success_message()



