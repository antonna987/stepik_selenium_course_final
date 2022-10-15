from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        input_password.send_keys(password)
        input_confirm_password = self.browser.find_element(
            *LoginPageLocators.REGISTER_CONFIRM_PASSWORD
        )
        input_confirm_password.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button_register.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "url doesn't contain 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_EMAIL
        ), "Login email is not presented"
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_PASSWORD
        ), "Login password is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_EMAIL
        ), "Register email is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_PASSWORD
        ), "Register password is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_CONFIRM_PASSWORD
        ), "Register confirm password is not presented"
