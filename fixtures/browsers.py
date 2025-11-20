from playwright.sync_api import Page, Playwright
import pytest

from pages.autentification.registration_page import RegistrationPage
from _pytest.fixtures import SubRequest

from tools.playwright.pages import initialize_playwright_page


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.form.fill(email='user.name@gmail.com', username='username', password='password')
    registration_page.registration_button.click()

    context.storage_state(path='browser-state.json')
    browser.close()


@pytest.fixture(scope='function')
def chromium_page_with_state(request: SubRequest, initialize_browser_state, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright, test_name=request.node.name, storage_state='browser-state.json')


@pytest.fixture(scope='function')
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright, test_name=request.node.name)
