import pytest
from pages.ya_search_page import YaSearchPage
from pages.ya_images_page import YaPictPage
from pages.locators import LINK, YaSearchPageLocators, YaPictPageLocators


@pytest.mark.skip
def test_images_link_presence(browser, link=LINK):
    page = YaSearchPage(browser, link)
    page.open()
    page.should_be_yandex_images_link()


@pytest.mark.skip
def test_yandex_images_is_opened(browser, link=LINK):
    page = YaPictPage(browser, link)
    page.open()
    page.get_element(*YaSearchPageLocators.YANDEX_PICTURES_LINK_CLICKABLE).click() #make method
    browser.switch_to.window(browser.window_handles[1])
    page.should_go_to_images_url()


@pytest.mark.skip
def test_first_images_category_is_opened(browser, link=LINK):
    page = YaPictPage(browser, link)
    page.open()
    page.get_element(*YaSearchPageLocators.YANDEX_PICTURES_LINK_CLICKABLE).click()
    browser.switch_to.window(browser.window_handles[1])
    curl = browser.current_url
    page.get_element(*YaPictPageLocators.IMAGES_FIRST_CATEGORY).click()
    page.first_category_should_be_opened(curl)


@pytest.mark.skip
def test_first_images_category_search_text_is_correct(browser, link=LINK):
    page = YaPictPage(browser, link)
    page.open()
    page.get_element(*YaSearchPageLocators.YANDEX_PICTURES_LINK_CLICKABLE).click()
    browser.switch_to.window(browser.window_handles[1])
    search_text = page.get_element(*YaPictPageLocators.IMAGES_FIRST_CATEGORY_SEARCH_TEXT).text
    page.get_element(*YaPictPageLocators.IMAGES_FIRST_CATEGORY).click()
    page.should_be_correct_text_in_search_input(search_text)


@pytest.mark.skip
def test_first_image_of_category_is_opened(browser, link=LINK):
    page = YaPictPage(browser, link)
    page.open()
    page.get_element(*YaSearchPageLocators.YANDEX_PICTURES_LINK_CLICKABLE).click()
    browser.switch_to.window(browser.window_handles[1])
    page.get_element(*YaPictPageLocators.IMAGES_FIRST_CATEGORY).click()
    page.get_element(*YaPictPageLocators.IMAGES_FIRST_IMAGE).click()
    page.first_picture_should_be_opened()


# @pytest.mark.skip
def test_image_is_changed_on_forward_button_click(browser, link=LINK):
    page = YaPictPage(browser, link)
    page.open()
    page.get_element(*YaSearchPageLocators.YANDEX_PICTURES_LINK_CLICKABLE).click()
    browser.switch_to.window(browser.window_handles[1])
    page.get_element(*YaPictPageLocators.IMAGES_FIRST_CATEGORY).click()
    page.get_element(*YaPictPageLocators.IMAGES_FIRST_IMAGE).click()
    first_img_src = page.get_element(*YaPictPageLocators.SLIDER_IMG_IS_OPENED).get_attribute('src')
    page.get_element(*YaPictPageLocators.SLIDER_FORWARD_BUTTON).click()
    current_img_src = page.get_element(*YaPictPageLocators.SLIDER_IMG_IS_OPENED).get_attribute('src')
    page.picture_should_change_on_fw_button_clicked(first_img_src, current_img_src)


# @pytest.mark.skip
def test_image_is_get_back_on_backward_button_click(browser, link=LINK):
    page = YaPictPage(browser, link)
    page.open()
    page.get_element(*YaSearchPageLocators.YANDEX_PICTURES_LINK_CLICKABLE).click()
    browser.switch_to.window(browser.window_handles[1])
    page.get_element(*YaPictPageLocators.IMAGES_FIRST_CATEGORY).click()
    page.get_element(*YaPictPageLocators.IMAGES_FIRST_IMAGE).click()
    first_img_src = page.get_element(*YaPictPageLocators.SLIDER_IMG_IS_OPENED).get_attribute('src')
    page.get_element(*YaPictPageLocators.SLIDER_FORWARD_BUTTON).click()
    page.get_element(*YaPictPageLocators.SLIDER_BACKWARD_BUTTON).click()
    current_img_src = page.get_element(*YaPictPageLocators.SLIDER_IMG_IS_OPENED).get_attribute('src')
    page.picture_should_get_back_to_the_same_on_bw_button_clicked(first_img_src, current_img_src)
