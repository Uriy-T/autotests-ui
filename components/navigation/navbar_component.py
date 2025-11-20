import allure

from components.base_component import BaseComponent
from playwright.sync_api import Page
from elements.text import Text


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.ui_course = Text(page, 'navigation-navbar-app-title-text', 'Navbar title')
        self.welcome_title = Text(page, 'navigation-navbar-welcome-title-text', 'Welcome message')

    @allure.step('Check that navbar component is visible and have text "UI Course" for user {username}')
    def check_visible(self, username: str):
        self.ui_course.check_visible()
        self.ui_course.check_have_text('UI Course')

        self.welcome_title.check_visible()
        self.welcome_title.check_have_text(f'Welcome, {username}!')
