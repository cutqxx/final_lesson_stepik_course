import time


def test_find_button(browser):
    #correct link:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    # not correct link:
    # link = "http://selenium1py.pythonanywhere.com/ru/"
    browser.get(link)
    time.sleep(30)
    assert browser.find_elements_by_css_selector("button.btn-add-to-basket"), "Button not find!"

