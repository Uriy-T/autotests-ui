from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.user_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.user_name_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.user_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        self.registration_button = page.get_by_test_id('registration-page-registration-button')


    def fill_registration_form(self, email: str, user_name: str, password: str):
        self.user_email_input.fill(email)
        expect(self.user_email_input).to_have_value(email)
        self.user_name_input.fill(user_name)
        expect(self.user_name_input).to_have_value(user_name)
        self.user_password_input.fill(password)
        expect(self.user_password_input).to_have_value(password)

    def click_registration_button(self):
        self.registration_button.click()