from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        login_link.click()

    def product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def added_product_name_should_be(self, expected):
        assert (
            self.added_product_name() == expected
        ), f"Expected '{expected}' product added, but got '{self.added_product_name()}'"

    def added_product_name(self):
        return self.browser.find_elements(*ProductPageLocators.MESSAGES)[0].text

    def basket_total_should_be(self, expected):
        assert (
            self.basket_total() == expected
        ), f"Expected '{expected}' basket total, but got '{self.basket_total()}'"

    def basket_total(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
