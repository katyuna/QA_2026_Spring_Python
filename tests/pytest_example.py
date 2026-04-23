from selenium import webdriver
from selenium.webdriver.common.by import By

# Запускать с помощью pytest -v -s
# Здесь не создается драйвер, потому чт о у pytest есть возможность

# Название функции долдно начинаться с test
def test_python_org_title(browser):
    browser.get('https://www.python.org')
    assert 'Python' in browser.page_source

def test_python_org_search_input(browser):
    browser.get('https://www.python.org')

    search_input = browser.find_element(By.NAME, 'q')
    search_input.clear()
    search_input.send_keys('Python')

    assert search_input.get_attribute('value') == 'Python'


