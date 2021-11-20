from selenium.webdriver.common.by import By

LINK = 'https://yandex.ru'


class YaSearchPageLocators:
    YANDEX_SEARCH_FIELD = (By.ID, "text")
    YANDEX_SUGGEST_POPUP_LIST = (By.CLASS_NAME, "mini-suggest__popup_visible")
    YANDEX_RESULT_LIST = (By.CLASS_NAME, "serp-list")
    YANDEX_PICTURES_LINK = (By.LINK_TEXT, "Картинки")
    YANDEX_PICTURES_LINK_CLICKABLE = (By.CSS_SELECTOR, 'a[data-id="images"]')


class YaPictPageLocators:
    IMAGES_FIRST_CATEGORY = (By.CSS_SELECTOR, ".PopularRequestList-Item_pos_0 .link,.Link")
    IMAGES_FIRST_CATEGORY_SEARCH_TEXT = (By.CSS_SELECTOR, ".PopularRequestList-Item_pos_0 "
                                                           ".PopularRequestList-SearchText")
    IMAGES_INPUT_BOX_TEXT = (By.CLASS_NAME, "input__control")
    IMAGES_INPUT_BOX = (By.CLASS_NAME, "input__box")
    IMAGES_FIRST_IMAGE = (By.CLASS_NAME, "serp-item_pos_0")

    SLIDER_IMG_IS_OPENED = (By.CLASS_NAME, "MMImage-Preview")
    SLIDER_IMG_SOURCE = (By.CLASS_NAME, "MMImage-Origin")
    SLIDER_FORWARD_BUTTON = (By.CLASS_NAME, "MediaViewer-ButtonNext")
    SLIDER_BACKWARD_BUTTON = (By.CLASS_NAME, "MediaViewer-ButtonPrev")
