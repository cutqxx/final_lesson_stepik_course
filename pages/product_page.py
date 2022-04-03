from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ProductPage(BasePage):
    # Добавление товара
    def should_click_to_basket(self):
        butt = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET)
        butt.click()
        self.solve_quiz_and_get_code()

    def assert_name_book_in_push_order(self):
        OR = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_OR).text
        FR = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_FR).text
        assert OR == FR, "Название книги в уведомлении не совпадает!"

    def assert_price_in_push_order(self):
        OR = self.browser.find_element(*ProductPageLocators.PRICE_OR).text
        FR = self.browser.find_element(*ProductPageLocators.PRICE_FR).text
        assert OR == FR, "Цена в уведомлении о заказе не совпадает!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Пуш об успехе появился, хотя не должен был"

    def should_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Пуш об успехе не исчезает"
