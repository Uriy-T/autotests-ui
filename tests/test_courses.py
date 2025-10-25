import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):

    courses_lbl = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    there_is_no_results_lbl = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    empty_block_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    description_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')

    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    expect(courses_lbl).to_be_visible()
    expect(courses_lbl).to_have_text('Courses')

    expect(empty_block_icon).to_be_visible()

    expect(there_is_no_results_lbl).to_be_visible()
    expect(there_is_no_results_lbl).to_have_text('There is no results')

    expect(description_block).to_be_visible()
    expect(description_block).to_have_text('Results from the load test pipeline will be displayed here')
