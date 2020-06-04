"""
Custom Showcase Base bike matrix checking.
"""
import sys
import allure
import pytest
from proj_poc.page.home_page import HomePage


@allure.feature("Check homepage")
@pytest.mark.parametrize('url', ["https://nae.poc.dev.local", "https://naefe.poc.dev.local"])
@pytest.mark.smoke
@pytest.mark.run(order=1)
def test_visit_homepage(firefox, url):
    """
    visit home page
    """
    err = 0
    homepage = HomePage(firefox)
    homepage.check_method("open homepage url", homepage.driver.get(url))
    homepage.check_method("check hero component amount", homepage.check_gallery_components_amount())
    homepage.check_method("screenshot home page", homepage.screenshot_homepage())
    homepage.check_method("check card component amount", homepage.check_card_components_amount())
    homepage.logger.info(homepage.err)
    if homepage.err:
        assert 0 == homepage.err



