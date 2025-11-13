import pytest

from pages.autentification.login_page import LoginPage
from pages.autentification.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.authotization
class TestAuthorization:
    @pytest.mark.parametrize('email, password',
                             [("user.name@gmail.com", "password"),
                              ("user.name@gmail.com", "  "),
                              ("  ", "password")
                              ])
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.form.fill(email=email, password=password)
        login_page.form.check_visible(email=email, password=password)
        login_page.click_login_button()
        login_page.check_validate_message_is_exist('Wrong email or password')

    def test_successful_authorization(self, registration_page: RegistrationPage,
                                             login_page: LoginPage,
                                             dashboard_page: DashboardPage):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.form.fill(email='test_user.name@gmail.com',
                                    username='test_username',
                                    password='test_pass')
        registration_page.click_registration_button()

        dashboard_page.navbar.check_visible('test_username')
        dashboard_page.sidebar.check_visible()
        dashboard_page.dashboard_title.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.form.fill(email='test_user.name@gmail.com', password='test_pass')
        login_page.click_login_button()

        dashboard_page.navbar.check_visible('test_username')
        dashboard_page.sidebar.check_visible()
        dashboard_page.dashboard_title.check_visible()

    def test_navigate_form_test_successful_authorization_to_registration(self,
                                                                         login_page: LoginPage,
                                                                         registration_page: RegistrationPage):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.click_registration()
        registration_page.form.check_visible(email='',
                                             username='',
                                             password='')


