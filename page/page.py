"""
Page Object, Base Page
"""
import os
import logging
from contextlib import contextmanager

import allure
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support import expected_conditions as EC

class Page(object):
    """基础类，用于所有页面的继承"""

    def __init__(self, driver, base_url=None):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30
        self.logger = logging.getLogger(__name__)
        self.err = 0

    # on_page()方法是URL地址的断言部分
    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    # _open()方法用于打开URL网站，并检验页面链接加载是否正确
    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        if "env" in os.environ and os.environ["env"] == "live":
            assert self.on_page(), f"Did not land on {url}"

    # open()方法通过调用_open()方法打开URL网站
    def open(self):
        self._open(self.url)

    # 重写定位元素的方法，loc==(By.NAME,"email"),是一个元组，Python方法中入参是元组时需要在前面加*
    def find_element(self, loc):
        return self.driver.find_element(*loc)

    def find_elements(self, loc):
        return self.driver.find_elements(*loc)

    def script(self, *src):
        return self.driver.execute_script(*src)

    # click element
    def click_element(self, loc, refresh_page=False, timeout=30):
        if refresh_page:
            with self.wait_for_page_load(timeout):
                self.find_element(loc).click()
        else:
            self.find_element(loc).click()

    # select element
    def select_element_by_value(self, loc, value, refresh_page=False, timeout=30):
        if refresh_page:
            with self.wait_for_page_load(timeout):
                Select(self.find_element(loc)).select_by_value(value)
        else:
            Select(self.find_element(loc)).select_by_value(value)

    # select element
    def select_element_by_index(self, loc, index, refresh_page=False, timeout=30):
        if refresh_page:
            with self.wait_for_page_load(timeout):
                Select(self.find_element(loc)).select_by_index(index)
        else:
            Select(self.find_element(loc)).select_by_index(index)

    # select element
    def select_element_by_visible_text(self, loc, text, refresh_page=False, timeout=30):
        if refresh_page:
            time.sleep(3)
            with self.wait_for_page_load(timeout):
                Select(self.find_element(loc)).select_by_visible_text(text)
        else:
            Select(self.find_element(loc)).select_by_visible_text(text)

    # textbox input value
    def input_element_value(self, loc, value):
        self.find_element(loc).clear()
        self.find_element(loc).send_keys(value)

    # mouseover element
    def mouseover_element(self, loc):
        action = ActionChains(self.driver)
        element = self.find_element(loc)
        action.move_to_element(element).perform()
        return element

    @contextmanager
    def wait_for_page_load(self, timeout=30):
        """
        wait for page load
        URL: https://blog.codeship.com/get-selenium-to-wait-for-page-load/
        :param timeout:
        :return:
        """
        old_page = self.driver.find_element_by_tag_name('html')
        yield
        WebDriverWait(self.driver, timeout).until(
            staleness_of(old_page)
        )

    # wait page element
    def wait_for_page_element(self, loc, timeout=30):
        return WebDriverWait(self.driver, timeout).until(loc)

    # get element text
    def get_element_text(self, loc):
        return self.find_element(loc).text

    # remove element from document
    def remove_element(self, loc):
        # element = self.find_element(loc)
        js = f"var element = document.querySelector(\"{loc[1]}\");element.remove();"
        self.driver.execute_script(js)

    def scroll_to_element(self, loc):
        """
        scroll to the element you select
        :param loc: element location
        :return: None
        """
        scroll_add_crowd_button = self.find_element(loc)
        # self.driver.execute_script("arguments[0].scrollIntoView();", scroll_add_crowd_button)
        self.script("arguments[0].scrollIntoView();", scroll_add_crowd_button)

    def scroll_to_distance(self, distance):
        """
        scroll to the distance
        :param distance: eg.1000
        :return:
        """
        js = f"document.documentElement.scrollTop={distance}"
        self.script(js)

    def take_full_screenshot(self, image_name):
        js = 'return Math.max( document.body.scrollHeight, document.body.offsetHeight,  document.documentElement.clientHeight,  document.documentElement.scrollHeight,  document.documentElement.offsetHeight);'
        scrollheight = self.driver.execute_script(js)
        height = self.driver.get_window_size()["height"] / 2
        offset = 0
        self.screenshot_path = f"report/screenshot/"
        if not os.path.exists(self.screenshot_path):
            os.mkdir(self.screenshot_path)
        while offset < scrollheight:
            self.driver.execute_script(f"window.scrollTo(0, {offset});" )
            offset += height
            time.sleep(0.3)
        '''
        while offset >= 0:
            self.driver.execute_script(f"window.scrollTo(0, {offset});")
            offset -= height
            time.sleep(0.3)
        '''
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)
        filename = f"{self.screenshot_path}/{image_name}.png"
        self.driver.find_element_by_tag_name('html').screenshot(filename)

    def wait_element_until_visible(self, loc, timeout=30):
        """
        wait for the element until it is visible
        :param loc: eg. By.ID, 'kw'
        :param timeout: default value is 30 seconds
        :return: the element you wait
        """
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of(self.find_element(loc)))

    def check_method(self,message, method=None):
        with allure.step(message):
            method_len = method
            if method_len:
                logging.warning(method_len)
                self.err += 1
            return self.err
