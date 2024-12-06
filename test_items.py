from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

def test_add_to_basket_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    browser.implicitly_wait(10)
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert type(add_to_basket_button) is WebElement
    print(add_to_basket_button.text)