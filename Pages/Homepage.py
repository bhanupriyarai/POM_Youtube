from Pages.Basepage import Basepage
from selenium.webdriver.common.by import By
from config.config import TestData
from selenium import webdriver

class Homepage(Basepage):

    l_title = (By.XPATH, "//a[@title='YouTube Home']")
    Search_Field = (By.ID, "search")
    Search_Button = (By.ID, "search-icon-legacy")

    """Constructor of page class"""
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver = driver
        # self.driver.get(TestData.Base_URL)


        """Page actions"""
        """Verify the page is correct"""
    def get_home_page_title(self, title):
        return self.get_title(title)

    def verify_page_title(self):
        return self.is_visible(self.l_title)

        """Enter search term and search"""
    def search_element(self, text):
        self.do_send_keys(self.Search_Field, text)
        self.do_click(self.Search_Button)

    def verify_page_link(self, ):
        return self.is_visible(TestData.Base_URL)



