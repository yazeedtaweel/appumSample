from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Locators.createInspectionPageLocators import *
from conftest import *


class CreateInspectionPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, pageElementsTimeOut)

    def click_start_inspection(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, start_Inspection_Button_CSS)))
        self.driver.find_element_by_css_selector(start_Inspection_Button_CSS).click()

    def get_start_inspection_text(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, start_Inspection_Button_CSS)))
        return self.driver.find_element_by_css_selector(start_Inspection_Button_CSS).text

    def check_start_inspection_button_visibility(self):
        try:
            return self.driver.find_element_by_css_selector(start_Inspection_Button_CSS).is_displayed()
        except:
            return 0
