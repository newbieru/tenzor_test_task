from pages.base_page import BasePage
from pages.locators import YaSearchPageLocators
from pages.locators import YaPictPageLocators


class YaPictPage(BasePage):
    def should_be_images_link(self):
        assert self.is_element_present(
            *YaSearchPageLocators.YANDEX_PICTURES_LINK), \
            "No 'https://yandex.ru/images/' link founded"

    def should_go_to_images_url(self):
        assert "https://yandex.ru/images/" in self.browser.current_url, \
            "Was not opened 'https://yandex.ru/images/'"

    def first_category_should_be_opened(self, url):
        assert url != self.browser.current_url, \
            "First category was not opened"

    def should_be_correct_text_in_search_input(self, search_text):
        assert search_text == self.get_element(
            *YaPictPageLocators.IMAGES_INPUT_BOX_TEXT).get_attribute('value'), \
            "Wrong search text"

    def first_picture_should_be_opened(self):
        assert self.is_element_present(*YaPictPageLocators.SLIDER_IMG_IS_OPENED), \
            "First picture was not opened"

    @staticmethod
    def picture_should_change_on_fw_button_clicked(current_img_src, next_img_src):
        assert current_img_src != next_img_src, \
            "Picture was not changed"

    @staticmethod
    def picture_should_get_back_to_the_same_on_bw_button_clicked(first_img_src, current_img_src):
        assert first_img_src == current_img_src, \
            "Current image is not the first image"


