from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Locators.ImagePreviewPageLocators import full_Screen_preview_Button_CSS
from Locators.InspectionPageLocators import *


class RightSideMenu:

    def click_skip_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, skip_Button_CSS)))
        self.driver.find_element_by_css_selector(skip_Button_CSS).click()

    def click_full_screen_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, full_Screen_preview_Button_CSS)))
        self.driver.find_element_by_css_selector(full_Screen_preview_Button_CSS).click()

    def click_take_photo_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, take_Photo_Button_CSS)))
        self.driver.find_element_by_css_selector(take_Photo_Button_CSS).click()

    def click_damage_detection_sensitivity_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, damage_Detection_Sensitivity_button_Css)))
        self.driver.find_element_by_css_selector(damage_Detection_Sensitivity_button_Css).click()
