from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.user_email = Input(page, 'registration-form-email-input', 'User_email_input')
        self.user_name = Input(page, 'registration-form-username-input', 'User_name_input')
        self.user_password = Input(page, 'registration-form-password-input', 'User_password_input')

    def fill(self, email: str, username: str, password: str):
        self.user_email.fill(email)
        self.user_name.fill(username)
        self.user_password.fill(password)

    def check_visible(self, email: str, username: str, password: str):
        self.user_email.check_visible()
        self.user_email.check_have_value(email)

        self.user_name.check_visible()
        self.user_name.check_have_value(username)

        self.user_password.check_visible()
        self.user_password.check_have_value(password)
