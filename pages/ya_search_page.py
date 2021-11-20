from pages.base_page import BasePage
from pages.locators import YaSearchPageLocators
from selenium.webdriver.common.by import By

counted = {0:'first',
           1:'second',
           2:'third',
           3:'fourth',
           4:'fifth'}


class YaSearchPage(BasePage):
    def should_be_search_input_field(self):
        assert self.is_element_present(*YaSearchPageLocators.YANDEX_SEARCH_FIELD), \
            "No search field founded"

    def should_be_popup_list(self):
        assert self.is_element_present(*YaSearchPageLocators.YANDEX_SUGGEST_POPUP_LIST), \
            "No popup list founded"

    def should_be_result_list(self):
        assert self.is_element_present(*YaSearchPageLocators.YANDEX_RESULT_LIST), \
            "No search result list founded"

    def should_be_yandex_images_link(self):
        assert self.is_element_present(*YaSearchPageLocators.YANDEX_PICTURES_LINK), \
            "No 'yandex.ru/images/' link founded"

    def should_be_tensor_ru_link_in_top_five_result(self, child):
        assert 'tensor.ru' in self.get_element(By.CSS_SELECTOR,
                                               f'.serp-list li[data-cid="{child}"] a').get_attribute('href'), \
            f'No "tensor.ru" pattern founded in {counted[child]} element of search result'

