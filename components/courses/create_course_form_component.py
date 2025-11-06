from playwright.sync_api import Page, expect
from components.base_component import BaseComponent


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.course_title_input = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.course_estimated_time_input = page.get_by_test_id('create-course-form-estimated-time-input').locator(
            'input')
        self.course_description = page.get_by_test_id('create-course-form-description-input').locator('textarea').first
        self.course_max_score = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.course_min_score = page.get_by_test_id('create-course-form-min-score-input').locator('input')

    def fill(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.course_title_input.fill(title)
        self.course_estimated_time_input.fill(estimated_time)
        self.course_description.fill(description)
        self.course_max_score.fill(max_score)
        self.course_min_score.fill(min_score)

    def check_visible(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        expect(self.course_title_input).to_be_visible()
        expect(self.course_title_input).to_have_value(title)

        expect(self.course_estimated_time_input).to_be_visible()
        expect(self.course_estimated_time_input).to_have_value(estimated_time)

        expect(self.course_description).to_be_visible()
        expect(self.course_description).to_have_value(description)

        expect(self.course_max_score).to_be_visible()
        expect(self.course_max_score).to_have_value(max_score)

        expect(self.course_min_score).to_be_visible()
        expect(self.course_min_score).to_have_value(min_score)
