"""
BOTK 2019 Home Page
"""
import allure
from selenium.webdriver.support.select import Select

from page.page import Page
from proj_poc.data.urls import current_url
from proj_poc.element.elements_define import ElementsDefine


class HomePage(Page):
    """
    Home Page
    """

    def __init__(self,driver):
        """
        init function
        :param driver:
        """
        self.url = "/"
        super(HomePage, self).__init__(driver, current_url())
        self.element = ElementsDefine()

    def check_navigation_bar(self):
        """
        check navigation is exist and the first one is HOME
        :return:
        """
        navigation = self.get_element_text(self.element.homepage_navigation)
        self.logger.info(navigation)
        if navigation != "HOME":
            return "The first one is not HOME"

    def screenshot_homepage(self):
        homepage_url = self.driver.current_url.split("//")[1].split(".")[0]
        screenshot_homepage_path = f"./report/screenshot/{homepage_url}_homepage.png"
        self.find_element(self.element.homepage_screenshot).screenshot(screenshot_homepage_path)
        with open(screenshot_homepage_path, mode='rb') as f:
            file = f.read()
            allure.attach(file, "homepage screenshot", allure.attachment_type.PNG)

    def check_gallery_components_amount(self):
        gallery_component = self.find_elements(self.element.homepage_gallery_component)
        if len(gallery_component) != 2:
            return f"Homepage have {len(gallery_component)} hero component, didn't equal to 2"

    def check_card_components_amount(self):
        card_components = self.find_elements(self.element.homepage_card_component)
        if len(card_components) != 6:
            return f"Homepage have {len(card_components)} card component, didn't equal to 6"
