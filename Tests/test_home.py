from Pages.Homepage import Homepage
from config.config import TestData
from Tests.Basetest import TestBase
from Pages.resultpage import resultpage
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Testhome(TestBase):

    def test_something(self):
        print('test_something')

    def test_browsersetup(self):
        self.driver.get(TestData.Base_URL)
        self.driver.maximize_window()

    def test_validate_URL(self):
        self.home = Homepage(self.driver)
        current = self.home.current_url(TestData.Base_URL)
        print("correct url")


    def test_youtube_title(self):
        self.home = Homepage(self.driver)
        title = self.home.get_title(TestData.TITLE_PAGE)
        assert title == TestData.TITLE_PAGE

    def test_validate_page_title(self):
        self.home = Homepage(self.driver)
        flag = self.home.verify_page_title()
        assert flag

    def test_search(self):
        self.home = Homepage(self.driver)
        self.home.search_element(TestData.SEARCH_TERM)

    def test_print_result(self):
        self.result = resultpage(self.driver)
        self.result.print_odd_result()
        self.result.select_10th()
        time.sleep(20)

