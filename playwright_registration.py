from playwright.sync_api import sync_playwright, expect
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    user_email = page.get_by_test_id('registration-form-email-input').locator('input')
    user_email.fill('user.name@gmail.com')

    user_name = page.get_by_test_id('registration-form-username-input').locator('input')
    user_name.fill('username')

    user_password = page.get_by_test_id('registration-form-password-input').locator('input')
    user_password.fill('password')

    btn_registration = page.get_by_test_id('registration-page-registration-button')
    btn_registration.click()


    dashboard_label = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_label).to_be_visible()
    expect(dashboard_label).to_have_text('Dashboard')

