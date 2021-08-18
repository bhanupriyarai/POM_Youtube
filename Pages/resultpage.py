from Pages.Basepage import Basepage
from selenium.webdriver.common.by import By
from config.config import TestData
from selenium import webdriver
import re

class resultpage(Basepage):


    result_list = (By.CSS_SELECTOR, "a[id='video-title']")

    """Constructor of page class"""
    def __init__(self, driver):
        super().__init__(driver)


        """Page actions"""

        """print all the odd numbered results"""
    def print_odd_result(self):
        b = self.get_element_text_from_list(self.result_list)
        # for x in range(len(b)):
        #     if x %2 !=0:
        #         print(b[x])

        # c = (re.search("title=", b)).group()
        print(b[0:7:2])

        """Select the 10th result"""
    def select_10th(self):
        x = self.get_element_text_from_list(self.result_list)
        y = x[10]
        self.select_by_text(self.result_list, y)





