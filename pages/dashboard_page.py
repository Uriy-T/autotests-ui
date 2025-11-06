from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from components.navigation.navbar_component import NavbarComponent
from components.navigation.side_bar_component import SidebarComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.charts.chart_view_component import ChartViewComponent


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = SidebarComponent(page)
        self.navbar = NavbarComponent(page)
        self.dashboard_title = DashboardToolbarViewComponent(page)
        self.student_chart_view = ChartViewComponent(page, identifier='students', chart_type='bar')
        self.activities_chart_view = ChartViewComponent(page, identifier='activities', chart_type='line')
        self.courses_chart_view = ChartViewComponent(page, identifier='courses', chart_type='pie')
        self.scores_chart_view = ChartViewComponent(page, identifier='scores', chart_type='scatter')

    #     self.student_chart_label = page.get_by_test_id('students-widget-title-text')
    #     self.student_chart = page.get_by_test_id('students-bar-chart')
    #
    #     self.activities_chart_label = page.get_by_test_id('activities-widget-title-text')
    #     self.activities_chart = page.get_by_test_id('activities-line-chart')
    #
    #     self.course_chart_label = page.get_by_test_id('courses-widget-title-text')
    #     self.course_chart = page.get_by_test_id('courses-pie-chart')
    #
    #     self.scores_chart_label = page.get_by_test_id('scores-widget-title-text')
    #     self.scores_chart = page.get_by_test_id('scores-scatter-chart')
    #
    # def check_studetns_card(self):
    #     expect(self.student_chart_label).to_be_visible()
    #     expect(self.student_chart_label).to_have_text('Students')
    #     expect(self.student_chart).to_be_visible()
    #
    # def check_activities_card(self):
    #     expect(self.activities_chart_label).to_be_visible()
    #     expect(self.activities_chart_label).to_have_text('Activities')
    #     expect(self.activities_chart).to_be_visible()
    #
    # def check_courses_card(self):
    #     expect(self.course_chart_label).to_be_visible()
    #     expect(self.course_chart_label).to_have_text('Courses')
    #     expect(self.course_chart).to_be_visible()
    #
    # def check_scores_card(self):
    #     expect(self.scores_chart_label).to_be_visible()
    #     expect(self.scores_chart_label).to_have_text('Scores')
    #     expect(self.scores_chart).to_be_visible()
