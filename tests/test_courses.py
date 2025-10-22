import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        user_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        user_name_input = page.get_by_test_id('registration-form-username-input').locator('input')
        user_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        registration_btn = page.get_by_test_id('registration-page-registration-button')

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        user_email_input.fill('test_user@gmail.com')
        user_name_input.fill('test_username')
        user_password_input.fill('test_password')
        registration_btn.click()

        context.storage_state(path='auth_context_practic.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='auth_context_practic.json')
        page = context.new_page()

        courses_lbl = page.get_by_test_id('courses-list-toolbar-title-text')
        there_is_no_results_lbl = page.get_by_test_id('courses-list-empty-view-title-text')
        empty_block_icon = page.get_by_test_id('courses-list-empty-view-icon')
        description_block = page.get_by_test_id('courses-list-empty-view-description-text')

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        expect(courses_lbl).to_be_visible()
        expect(courses_lbl).to_have_text('Courses')

        expect(empty_block_icon).to_be_visible()

        expect(there_is_no_results_lbl).to_be_visible()
        expect(there_is_no_results_lbl).to_have_text('There is no results')

        expect(description_block).to_be_visible()
        expect(description_block).to_have_text('Results from the load test pipeline will be displayed here')
