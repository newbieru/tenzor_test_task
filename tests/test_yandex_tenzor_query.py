import pytest
from pages.ya_search_page import YaSearchPage
from pages.locators import LINK, YaSearchPageLocators
from selenium.webdriver.common.keys import Keys



# @pytest.mark.skip
def test_yandex_ru_search_input_presence(browser, link=LINK):
    page = YaSearchPage(browser, link)
    page.open()
    page.should_be_search_input_field()


# @pytest.mark.skip
def test_yandex_ru_search_suggest_popup_list_presence(browser, link=LINK):
    page = YaSearchPage(browser, link)
    page.open()
    search_input = page.browser.find_element(*YaSearchPageLocators.YANDEX_SEARCH_FIELD)
    # search_input = page.get_element(*YaSearchPageLocators.YANDEX_SEARCH_FIELD)
    search_input.send_keys('Тензор')
    page.should_be_popup_list()


# @pytest.mark.skip
def test_yandex_search_result_list_presence(browser, link=LINK):
    page = YaSearchPage(browser, link)
    page.open()
    search_input = page.get_element(*YaSearchPageLocators.YANDEX_SEARCH_FIELD)
    search_input.send_keys('Тензор')
    search_input.send_keys(Keys.ENTER)
    page.should_be_result_list()


@pytest.mark.xfail
@pytest.mark.parametrize('children', range(5))
def test_yandex_search_top_five_result_contain_tensor_ru(browser, children, link=LINK):
    page = YaSearchPage(browser, link)
    page.open()
    search_input = page.get_element(*YaSearchPageLocators.YANDEX_SEARCH_FIELD)
    search_input.send_keys('Тензор')
    search_input.send_keys(Keys.ENTER)
    page.should_be_tensor_ru_link_in_top_five_result(children)
