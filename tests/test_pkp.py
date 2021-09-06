import pytest
from selenium.webdriver import Chrome
from pages import searchPage
from pages import resultsPage
import os

@pytest.fixture(scope='class')
def browser_create(request):
    path = os.path.dirname(os.path.abspath(__file__))
    driver = Chrome(os.path.join(path, 'chromedriver'))
    driver.implicitly_wait(15)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures('browser_create')
class TestBasic:
    pass
class TestResultsPageTest(TestBasic):

    def test_find_minimum_transfers(self):
        search = searchPage.pkpSearchPage(self.driver)
        search.load()
        search.eatCookies().click()
        search.closeAdds().click()
        search.searchConnection("Kraków Główny", "Lausanne")

        results = resultsPage.resultsPage(self.driver)
        results.findBestConnection()
        results.printResults()