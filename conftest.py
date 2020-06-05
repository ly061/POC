"""
pytest conftest file
"""
import os
import pytest
from selenium import webdriver
import shutil

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="env option: dev/staging/live")
    parser.addoption("--headless", action="store", default="False", help="headless option: True/False")

def pytest_configure(config):
    os.environ["env"] = config.getoption("env")

@pytest.fixture(name='chrome')
def chrome_browser(request):
    option = webdriver.ChromeOptions()
    option.headless = request.config.getoption("headless")
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(name='firefox')
def firefox_browser(request):
    option = webdriver.FirefoxOptions()
    option.headless = request.config.getoption("headless")
    driver = webdriver.Firefox(options=option)
    driver.maximize_window()
    yield driver
    driver.quit()

# def pytest_sessionstart():
#     if not os.path.exists("report/xml"):
#         os.mkdir("report/xml")
#     else:
#         shutil.rmtree("report/xml")
#         os.mkdir("report/xml")
#     if not os.path.exists("report/allure"):
#         os.mkdir("report/allure")
#     else:
#         shutil.rmtree("report/allure")
#         os.mkdir("report/allure")
#     print("cleaning data over")

# def pytest_sessionfinish(session):
#     """
#     开几个线程就会执行几次
#     """
#     allure_dir = session.config.getoption('allure_report_dir')
#     if allure_dir:
#         os.system(f"allure generate report/xml -o report/allure --clean")
#         os.system(f"allure open report/allure")

