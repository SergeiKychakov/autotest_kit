import pytest
from .pages.product_page import PageObject

@pytest.mark.parametrize('promo_offer', ["1", "2", "3", "4", "5", "6", "7", "8", "9"])
@pytest.mark.parametrize('link', ["okay_link", pytest.param("bugged_link", marks=pytest.mark.xfail), "okay_link"])

def test_guest_can_add_product_to_basket(browser, promo_offer, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = PageObject(browser, link)  # инициализируем Page Object, 
    # передаем в конструктор экземпляр драйвера и url адрес 
    page.open() # открываем страницу
    page.add_to_basket() # добавляем книгу в корзину
    page.count_in_allert_example() # считаем значание в алерте и нажимаем ОК
    #page.checking() # проверка наличия книги и соответствие цены
    