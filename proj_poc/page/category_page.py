"""
Custom show case Category Page
"""


import os
import datetime,time
from page.page import Page
from proj_poc.data.urls import current_url
from proj_poc.element.elements_define import ElementsDefine

class CategoryPage(Page):
    """
    Custom show case Category Page
    """

    def __init__(self, driver):
        """
        init function
        :param driver:
        """
        self.format_url = "/{}/pick-a-category"
        super(CategoryPage, self).__init__(driver, current_url())
        self.element = ElementsDefine()

        self.screenshot_path = f"report/screenshot/proj-{datetime.datetime.now():%Y%m%d}"
        if not os.path.exists(self.screenshot_path):
            os.mkdir(self.screenshot_path)

    def take_screenshot(self, locale, page):
        filename = f"{self.screenshot_path}/{locale}-{datetime.datetime.now():%Y%m%d%H%M%S}-{page}.png"
        self.driver.find_element_by_tag_name('html').screenshot(filename)