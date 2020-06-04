"""
Custom Showcase Base bike matrix checking.
"""
import allure
import pytest

from proj_poc.data.marketmatrix_utils import *
from proj_poc.page.category_page import CategoryPage


@allure.story("Check Locale Bike List")
@pytest.mark.parametrize('locale',
                         ["de_AT", "de_DE", "fr_BE", "nl_BE", "fr_LU", "nl_NL", "en_GB", "en_IE", "es_ES", "pt_PT",
                          "fr_FR", "it_IT", "en_CA", "fr_CA", "es_MX", "ja_JP", "en_IN", "pt_BR"])
def test_base_bike_matrix(firefox, locale):
    current_page = CategoryPage(firefox)
    # open category page
    current_page.url = current_page.format_url.format(locale)
    current_page.open()

    bike_list = get_bike_matrix()[locale]

    # all category
    category_cards = current_page.find_elements(current_page.element.categories_category_card)
    category_links = []
    for cc in category_cards:
        # title = cc.find_element_by_css_selector("div.categoryList__card div.categoryList__card-title").text.strip()
        link = cc.find_element_by_css_selector("a.categoryList__link").get_attribute('href')
        title = link.split('/')[-1]
        category_links.append({'title': title, 'link': link})

    testcase_flag = True
    for cl in category_links:
        allure.attach(f"Open locale: {locale}, category: {cl['title']}")
        current_page.driver.get(cl['link'])
        assert cl['link'] == current_page.driver.current_url, f"[{locale}]:[{cl['title']}] url is incorrect. Expect:[{cl['link']}], Actual: [{current_page.driver.current_url}]"

        show_me_more = current_page.find_elements(current_page.element.basebike_show_me_more)
        if show_me_more:
            show_me_more[0].click()

        # take screenshot
        current_page.remove_element(current_page.element.homepage_header_menu_panel)
        current_page.take_screenshot(locale, cl['title'])

        bike_list_panel = current_page.find_elements(current_page.element.basebike_find_dealer)
        page_bike_model = [bike.get_attribute('href').split('=')[1] for bike in bike_list_panel]

        matrix_bike_model = bike_list[cl['title']]

        if sorted(matrix_bike_model) != sorted(page_bike_model):
            testcase_flag = False
            current_page.logger.error(
                f"[{locale}][{cl['title']}], bike list is incorrect, Expect:[{sorted(matrix_bike_model)}], Actual:[{sorted(page_bike_model)}]")
        else:
            current_page.logger.info(
                f"[{locale}][{cl['title']}], bike list is correct, Expect:[{sorted(matrix_bike_model)}], Actual:[{sorted(page_bike_model)}]")
        allure.attach(f'Finished locale: {locale}')
        assert testcase_flag, f"[{locale}] bike list error, please see log for more info."
