from playwright.sync_api import Page, expect
from typing import Pattern
import allure

class BaseComponent:
    def __init__(self, page:Page):
        self.page = page

    @allure.step('Check that actual url is equal expected url pattern: {expected_url}')
    def check_current_url(self, expected_url: Pattern[str]):
        expect(self.page).to_have_url(expected_url)