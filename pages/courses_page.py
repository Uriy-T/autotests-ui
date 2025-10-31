from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class CoursesList(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # divide: Элементы заголовка
        self.courses_main_lable = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('courses-list-toolbar-create-course-button')

        # divide: Элементы страницы без курсов
        self.empty_course_icon = page.get_by_test_id('courses-list-empty-view-icon')
        self.no_results_label = page.get_by_test_id('courses-list-empty-view-title-text')
        self.no_results_description = page.get_by_test_id('courses-list-empty-view-description-text')

        # divide: Элементы карточки курса
        self.course_card_label = page.get_by_test_id('course-widget-title-text')
        self.course_image = page.get_by_test_id('course-preview-image')
        self.max_score_text = page.get_by_test_id('course-max-score-info-row-view-text')
        self.min_score_text = page.get_by_test_id('course-min-score-info-row-view-text')
        self.estimated_time = page.get_by_test_id('course-estimated-time-info-row-view-text')

        # divide: Элементы меню карточки курса
        self.course_card_menu_button = page.get_by_test_id('course-view-menu-button')
        self.course_edit_button = page.get_by_test_id('course-view-edit-menu-item-text')
        self.course_delete_button = page.get_by_test_id('course-view-delete-menu-item')


    def check_courses_main_label(self):
        expect(self.courses_main_lable).to_be_visible()
        expect(self.courses_main_lable).to_have_text('Courses')

    def click_create_course_button(self):
        self.create_course_button.click()

    def check_visible_create_course_button(self):
        expect(self.create_course_button).to_be_visible()

    def check_content_block(self):
        expect(self.empty_course_icon).to_be_visible()
        expect(self.no_results_label).to_be_visible()
        expect(self.no_results_label).to_have_text('There is no results')
        expect(self.no_results_description).to_be_visible()
        expect(self.no_results_label).to_have_text('Results from the load test pipeline will be displayed here')

    def check_course_card(
            self,
            index: int,
            label: str,
            max_score: str,
            min_score: str,
            estimated_time: str
    ):
        expect(self.course_image.nth(index)).to_be_visible()

        expect(self.course_card_label.nth(index)).to_be_visible()
        expect(self.course_card_label.nth(index)).to_have_text(label)

        expect(self.max_score_text.nth(index)).to_be_visible()
        expect(self.max_score_text.nth(index)).to_have_text(f'Max score: {max_score}')

        expect(self.min_score_text.nth(index)).to_be_visible()
        expect(self.min_score_text.nth(index)).to_have_text(f'Min score: {min_score}')

        expect(self.estimated_time.nth(index)).to_be_visible()
        expect(self.estimated_time.nth(index)).to_have_text(f'Estimated time: {estimated_time}')

    def click_edit_course_button(self, index: int):
        self.course_card_menu_button.nth(index).click()

        expect(self.course_edit_button.nth(index)).to_be_visible()
        self.course_edit_button.nth(index).click()

    def click_delete_course_button(self, index):
        self.course_card_menu_button.nth(index).click()

        expect(self.course_delete_button.nth(index)).to_be_visible()
        self.course_delete_button.nth(index).click()