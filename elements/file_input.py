from playwright.sync_api import Locator

from elements.base_element import BaseElement


class FileInput(BaseElement):
    def get_locator(self, **kwargs) -> Locator:
        return super().get_locator(**kwargs).locator('input')

    def set_input_files(self, path: str, **kwargs):
        locator = self.get_locator(**kwargs)
        locator.set_input_files(path)

