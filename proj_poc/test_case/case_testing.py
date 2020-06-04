import pytest
from selenium import webdriver


@pytest.mark.test
def test_demo():
    driver = webdriver.Firefox()
    driver.get("https://www.baidu.com")
