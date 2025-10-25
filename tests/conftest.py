from playwright.sync_api import sync_playwright, Page, Playwright
import pytest


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    user_email = page.get_by_test_id('registration-form-email-input').locator('input')
    user_email.fill('user.name@gmail.com')

    user_name = page.get_by_test_id('registration-form-username-input').locator('input')
    user_name.fill('username')

    user_password = page.get_by_test_id('registration-form-password-input').locator('input')
    user_password.fill('password')

    btn_registration = page.get_by_test_id('registration-page-registration-button')
    btn_registration.click()

    context.storage_state(path='browser-state.json')



@pytest.fixture(scope='function')
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    yield context.new_page()
