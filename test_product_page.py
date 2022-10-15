from time import time
from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    product_name = page.product_name()
    product_price = page.product_price()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.added_product_name_should_be(product_name)
    page.basket_total_should_be(product_price)
