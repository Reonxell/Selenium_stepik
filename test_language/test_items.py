import time


def test_items(app):
    app.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    assert app.find_element_by_css_selector(
        '.btn-add-to-basket').is_displayed() == True, 'Кнопка добавления в корзину не кативна'
