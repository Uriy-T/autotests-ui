from playwright.sync_api import Locator

from elements.base_element import BaseElement


class FileInput(BaseElement):
    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(nth, **kwargs).locator('input')

    def set_input_files(self, path: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        locator.set_input_files(path)

