import pytest
import allure
from allure_commons.types import Severity

from pages.autentification.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage

from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStories
from tools.allure.features import AllureFeatures


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTags.REGRESSION, AllureTags.REGISTRATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeatures.AUTHENTICATION)
@allure.story(AllureStories.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeatures.AUTHENTICATION)
@allure.sub_suite(AllureStories.REGISTRATION)
class TestRegistration:

    @allure.title('Registration with correct email, username and password')
    @allure.severity(Severity.BLOCKER)
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.form.fill(email='user.name@gmail.com',
                                    username='username',
                                    password='password')
        registration_page.form.check_visible(email='user.name@gmail.com',
                                             username='username',
                                             password='password')
        registration_page.click_registration_button()
        dashboard_page.dashboard_title.check_visible()
