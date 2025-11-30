from playwright.sync_api import Locator

from elements.base_element import BaseElement
import allure

from tools.logger import get_logger

logger = get_logger('FILE_INPUT')


class FileInput(BaseElement):

    @property
    def type_of(self) -> str:
        return 'file input'

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(nth, **kwargs).locator('input')

    def set_input_files(self, path: str, nth: int = 0, **kwargs):
        step = f'Set file "{path}" to the {self.type_of} with {self.name}'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.set_input_files(path)
