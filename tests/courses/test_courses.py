import allure
import pytest
from allure_commons.types import Severity

from pages.courses.new_course_creation_page import CreateCoursePage
from pages.courses.courses_list_page import CoursesListPage

from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStories
from tools.allure.features import AllureFeatures


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTags.COURSES, AllureTags.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeatures.COURSES)
@allure.story(AllureStories.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeatures.COURSES)
@allure.sub_suite(AllureStories.COURSES)
class TestCourses:

    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        courses_list_page.navbar.check_visible('username')
        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.course_toolbar.check_visible(is_create_course_disabled=True)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(title='',
                                                            description='',
                                                            estimated_time='',
                                                            max_score='0',
                                                            min_score='0')
        create_course_page.exercises_toolbar.check_visible()
        create_course_page.exercises_empty_view.check_visible(title='There is no exercises',
                                                              description='Click on "Create exercise" button to create new exercise')
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(title='Playwright',
                                                   estimated_time='2 weeks',
                                                   description='Playwright',
                                                   max_score='100',
                                                   min_score='10')
        create_course_page.course_toolbar.create_course_button.click()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(index=0,
                                                    label='Playwright',
                                                    estimated_time='2 weeks',
                                                    max_score='100',
                                                    min_score='10')

    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.create_course_form.fill(title='Playwright for Python',
                                                   estimated_time='2 weeks',
                                                   description='Playwright study',
                                                   max_score='100',
                                                   min_score='10')
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.course_toolbar.create_course_button.click()
        courses_list_page.course_view.check_visible(index=0,
                                                    label='Playwright for Python',
                                                    estimated_time='2 weeks',
                                                    max_score='100',
                                                    min_score='10')

        courses_list_page.course_view.menu.click_edit(index=0)

        create_course_page.create_course_form.fill(title='Requests for Python',
                                                   estimated_time='3 weeks',
                                                   description='API Testing with Python',
                                                   max_score='120',
                                                   min_score='15')
        create_course_page.course_toolbar.create_course_button.click()

        courses_list_page.course_view.check_visible(index=0,
                                                    label='Requests for Python',
                                                    estimated_time='3 weeks',
                                                    max_score='120',
                                                    min_score='15')
