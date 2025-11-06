from playwright.sync_api import Page, expect
from components.base_component import BaseComponent


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.user_email = page.get_by_test_id('registration-form-email-input').locator('input')
        self.user_name = page.get_by_test_id('registration-form-username-input').locator('input')
        self.user_password = page.get_by_test_id('registration-form-password-input').locator('input')

    def fill(self, email: str, username: str, password: str):
        self.user_email.fill(email)
        self.user_name.fill(username)
        self.user_password.fill(password)

    def check_visible(self, email: str, username: str, password: str):
        expect(self.user_email).to_be_visible()
        expect(self.user_email).to_have_value(email)

        expect(self.user_name).to_be_visible()
        expect(self.user_name).to_have_value(username)

        expect(self.user_password).to_be_visible()
        expect(self.user_password).to_have_value(password)
