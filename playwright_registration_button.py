from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    user_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    user_name_input = page.get_by_test_id('registration-form-username-input').locator('input')
    user_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_btn = page.get_by_test_id('registration-page-registration-button')

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    expect(registration_btn).to_be_disabled()
    user_email_input.fill('user.name@gmail.com')
    user_name_input.fill('username')
    user_password_input.fill('password')
    expect(registration_btn).to_be_enabled()
