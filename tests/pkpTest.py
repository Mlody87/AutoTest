import pytest
from selenium.webdriver import Chrome
from pages import searchPage
from pages import resultsPage
import os

@pytest.fixture
def browser():
    path = os.path.dirname(os.path.abspath(__file__))
    driver = Chrome(os.path.join(path, 'chromedriver'))
    driver.implicitly_wait(15)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_minNumberOfTransfers(browser):
    search = searchPage.pkpSearchPage(browser)
    search.load()
    search.eatCookies().click()
    search.closeAdds().click()
    search.searchConnection("Kraków Główny", "Lausanne")

    results = resultsPage.resultsPage(browser)
    results.findBestConnection()
    results.printResults()