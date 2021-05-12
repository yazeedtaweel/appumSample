from Locators.InspectionPageLocators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LeftSideMenu:

    def open_menu(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, burger_Menu_Button_CSS)))
        self.driver.find_element_by_css_selector(burger_Menu_Button_CSS).click()

    def close_menu(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, close_Menu_Css)))
        self.driver.find_element_by_css_selector(close_Menu_Css).click()

    def click_cancel_scan_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, cancel_Scan_Button_CSS)))
        self.driver.find_element_by_css_selector(cancel_Scan_Button_CSS).click()

    def click_cancel_scan_icon(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, cancel_Scan_Icon_CSS)))
        self.driver.find_element_by_css_selector(cancel_Scan_Icon_CSS).click()

    def get_cancel_scan_button_text(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, cancel_Scan_Span_CSS)))
        return self.driver.find_element_by_css_selector(cancel_Scan_Span_CSS).text

    def make_sure_menu_is_closed(self):
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, close_Menu_Css)))
        return 1



