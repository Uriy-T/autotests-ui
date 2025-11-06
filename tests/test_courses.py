import pytest
from pages.new_course_creation_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    courses_list_page.navbar.check_visible('username')
    courses_list_page.sidebar.check_visible()

    courses_list_page.toolbar_view.check_visible()
    courses_list_page.check_visible_empty_view()


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
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
