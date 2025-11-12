from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.text_area import TextArea
from elements.input import Input

class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.course_title_input = Input(page,'create-course-form-title-input', 'Course title input')
        self.course_estimated_time_input = Input(page,'create-course-form-estimated-time-input','Estimated time')
        self.course_description = TextArea(page, 'create-course-form-description-input', 'Description input')
        self.course_max_score = Input(page,'create-course-form-max-score-input', 'Max score input')
        self.course_min_score = Input(page,'create-course-form-min-score-input', 'Max score input')

    def fill(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.course_title_input.fill(title)
        self.course_estimated_time_input.fill(estimated_time)
        self.course_description.fill(description)
        self.course_max_score.fill(max_score)
        self.course_min_score.fill(min_score)

    def check_visible(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.course_title_input.check_visible()
        self.course_title_input.check_have_value(title)

        self.course_estimated_time_input.check_visible()
        self.course_estimated_time_input.check_have_value(estimated_time)

        self.course_description.check_visible()
        self.course_description.check_have_value(description)

        self.course_max_score.check_visible()
        self.course_max_score.check_have_value(max_score)

        self.course_min_score.check_visible()
        self.course_min_score.check_have_value(min_score)
