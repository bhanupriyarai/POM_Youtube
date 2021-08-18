from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Basepage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))
        return element.text

    def get_element_text_from_list(self, by_locator):
        elements_text = []
        element_list = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))
        for element in element_list:
            elements_text.append(element.text)
        return elements_text

    def select_by_text(self, by_locator, text):
        element_list = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))
        for element in element_list:
            if element.text == text:
                element.click()
                break


    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def get_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))
        return element

    def current_url(self, url):
        element = WebDriverWait(self.driver, 10).until(EC.url_contains(url))
        return bool(element)


