import pytest
import allure
from allure_commons.types import Severity

from pages.dashboard.dashboard_page import DashboardPage

from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStories
from tools.allure.features import AllureFeatures
from tools.routes import AppRoute
from config import settings


@pytest.mark.dashboard
@pytest.mark.regression
@allure.tag(AllureTags.DASHBOARD, AllureTags.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeatures.DASHBOARD)
@allure.story(AllureStories.DASHBOARD)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeatures.DASHBOARD)
@allure.sub_suite(AllureStories.DASHBOARD)
class TestDashboard:

    @allure.severity(Severity.NORMAL)
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit(AppRoute.DASHBOARD)
        dashboard_page_with_state.navbar.check_visible(settings.test_user.username)
        dashboard_page_with_state.sidebar.check_visible()

        dashboard_page_with_state.dashboard_title.check_visible()
        dashboard_page_with_state.student_chart_view.check_visible('Students')
        dashboard_page_with_state.activities_chart_view.check_visible('Activities')
        dashboard_page_with_state.courses_chart_view.check_visible('Courses')
        dashboard_page_with_state.scores_chart_view.check_visible('Scores')
