from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEMS
        ), "Expected empty basket, but no"

    def should_be_empty_message(self):
        assert (
            "Your basket is empty."
            in self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text
        ), "Expected message 'Your basket is empty.', but there is no"
