import pytest
import allure
from allure_commons.types import Severity

from pages.autentification.login_page import LoginPage
from pages.autentification.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage

from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStories
from tools.allure.features import AllureFeatures
from tools.routes import AppRoute
from config import settings


@pytest.mark.regression
@pytest.mark.authotization
@allure.tag(AllureTags.AUTHORISATION, AllureTags.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeatures.AUTHENTICATION)
@allure.story(AllureStories.AUTHORIZATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeatures.AUTHENTICATION)
@allure.sub_suite(AllureStories.AUTHORIZATION)
class TestAuthorization:
    @pytest.mark.xdist_group(name='authorization-group')
    @pytest.mark.parametrize('email, password',
                             [("user.name@gmail.com", "password"),
                              ("user.name@gmail.com", "  "),
                              ("  ", "password")
                              ])
    @allure.title('Wrong email or password authorization')
    @allure.tag(AllureTags.USER_LOGIN)
    @allure.severity(Severity.CRITICAL)
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit(AppRoute.LOGIN)
        login_page.form.fill(email=email, password=password)
        login_page.form.check_visible(email=email, password=password)
        login_page.click_login_button()
        login_page.check_validate_message_is_exist('Wrong email or password')

    @allure.title('Navigation from login page to registration page')
    @allure.tag(AllureTags.NAVIGATION)
    @allure.severity(Severity.NORMAL)
    def test_navigate_form_authorization_to_registration(self, login_page: LoginPage,
                                                         registration_page: RegistrationPage):
        login_page.visit(AppRoute.LOGIN)
        login_page.click_registration()
        registration_page.form.check_visible(email='',
                                             username='',
                                             password='')

    @allure.title('User login with correct email and password')
    @allure.tag(AllureTags.USER_LOGIN)
    @allure.severity(Severity.BLOCKER)
    def test_successful_authorization(self, registration_page: RegistrationPage,
                                      login_page: LoginPage,
                                      dashboard_page: DashboardPage):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.form.fill(email=settings.test_user.email,
                                    username=settings.test_user.username,
                                    password=settings.test_user.password)
        registration_page.click_registration_button()

        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.sidebar.check_visible()
        dashboard_page.dashboard_title.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.form.fill(email=settings.test_user.email, password=settings.test_user.password)
        login_page.click_login_button()

        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.sidebar.check_visible()
        dashboard_page.dashboard_title.check_visible()
