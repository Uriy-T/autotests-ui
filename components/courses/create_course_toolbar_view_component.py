import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_courses_main_label = Text(page, 'create-course-toolbar-title-text', 'Create course toolbar title')
        self.create_course_button = Button(page, 'create-course-toolbar-create-course-button', 'Create course button')

    @allure.step('Check that create course toolbar view component is visible')
    def check_visible(self, is_create_course_disabled=True):
        self.create_courses_main_label.check_visible()
        self.create_courses_main_label.check_have_text('Create course')

        self.create_course_button.check_visible()

        if is_create_course_disabled:
            self.create_course_button.check_disabled()
        else:
            self.create_course_button.check_enabled()

    def click_create_course_button(self):
        self.create_course_button.click()
