import time
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_quest_should_see_button(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    add_button=browser.find_elements_by_css_selector("#add_to_basket_form1")
    assert len(add_button)>0, "button not found"
