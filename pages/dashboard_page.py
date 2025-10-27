from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_label = page.get_by_test_id('dashboard-toolbar-title-text')

    def check_dashboard_label(self):
        expect(self.dashboard_label).to_be_visible()
        expect(self.dashboard_label).to_have_text('Dashboard')