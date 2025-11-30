import pytest
from playwright.sync_api import Page
from pages.autentification.login_page import LoginPage
from pages.autentification.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.new_course_creation_page import CreateCoursePage

@pytest.fixture(scope='function')
def login_page(page: Page) -> LoginPage:
    return LoginPage(page=page)

@pytest.fixture(scope='function')
def registration_page(page: Page) -> RegistrationPage:
    return RegistrationPage(page=page)

@pytest.fixture(scope='function')
def dashboard_page(page: Page) -> DashboardPage:
    return DashboardPage(page=page)

@pytest.fixture(scope='function')
def dashboard_page_with_state(page_with_state: Page) -> DashboardPage:
    return DashboardPage(page=page_with_state)

@pytest.fixture(scope='function')
def courses_list_page(page_with_state: Page) -> CoursesListPage:
    return CoursesListPage(page=page_with_state)

@pytest.fixture(scope='function')
def create_course_page(page_with_state: Page) -> CreateCoursePage:
    return CreateCoursePage(page=page_with_state)