from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.input import Input


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.user_email = Input(page, 'login-form-email-input', 'Email input')
        self.user_password = Input(page, 'login-form-password-input', 'Password input')

    def fill(self, email: str, password: str):
        self.user_email.fill(email)
        self.user_password.fill(password)

    def check_visible(self, email: str, password: str):
        self.user_email.check_visible()
        self.user_email.check_have_value(email)

        self.user_password.check_visible()
        self.user_password.check_have_value(password)
