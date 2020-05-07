link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'

def test_quest_should_see_button(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert button.text == 'Ajouter au panier', \
        'not found button'