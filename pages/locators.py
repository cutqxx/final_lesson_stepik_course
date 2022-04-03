from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON_ADD_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME_OR = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_FR = (By.CSS_SELECTOR, "div.alert-success div.alertinner strong")
    PRICE_OR = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRICE_FR = (By.CSS_SELECTOR, "div.alert-info div.alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")