from playwright.sync_api import Page

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

