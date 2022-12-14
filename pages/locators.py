from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (
        By.CSS_SELECTOR,
        "#default > header > div > div > div.basket-mini > span > a",
    )
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")

    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators:
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, "#messages > div")
    PRODUCT_NAME = (
        By.CSS_SELECTOR,
        "#content_inner > article > div.row > div.col-sm-6.product_main > h1",
    )
    PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color",
    )
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGES = (By.CSS_SELECTOR, "#messages > div > div > strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages > div > div > p > strong")


class BasketPageLocators:
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items > div.row")
