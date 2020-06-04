"""
BOTK 2019 landing page checking.
"""

import pytest
import allure

from proj_poc.page.landing_page import LandingPage


def _test_get_locale(chrome):
    landing_page = LandingPage(chrome)
    landing_page.open()
    locales = landing_page.get_all_locales()
    landing_page.logger.info(locales)


@allure.story('Check Locale Homepage')
@pytest.mark.parametrize('locale', ["de_AT", "de_DE", "fr_BE", "nl_BE", "fr_LU", "nl_NL", "en_GB", "en_IE", "es_ES", "pt_PT", "fr_FR", "it_IT", "en_CA", "fr_CA", "es_MX", "ja_JP", "en_IN", "pt_BR"])
def test_check_home_page(firefox, locale):
    landing_page = LandingPage(firefox)
    # open landing page
    landing_page.open()
    # country select
    landing_page.select_element_by_value(landing_page.element.landing_country_select, locale)
    # button click
    landing_page.click_element(landing_page.element.landing_continue_button, refresh_page=True)
    # check
    assert locale in landing_page.driver.current_url
