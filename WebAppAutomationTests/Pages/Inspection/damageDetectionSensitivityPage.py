from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Locators.damageDetectionPageLocators import *


class DamageDetectionSensitivity:

    def make_sure_back_button_existed_threshold_page(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                              back_Button_Damage_Detection_Sensitivity_Css)))
            return True
        except:
            return False

    def make_sure_refresh_button_existed_threshold_page(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                              refresh_Button_Damage_Detection_Sensitivity_Css)))
            return True
        except :
            return False

    def get_closeup_sensitivity_field_text(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                          closeup_Sensitivity_Field_Damage_Detection_Sensitivity_Css)))
        return self.driver.find_element_by_css_selector(closeup_Sensitivity_Field_Damage_Detection_Sensitivity_Css).text

    def get_full_view_sensitivity_field_text(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                          full_View_Sensitivity_Field_Damage_Detection_Sensitivity_Css)))
        return self.driver.find_element_by_css_selector(full_View_Sensitivity_Field_Damage_Detection_Sensitivity_Css).text

    def click_back_button_threshold_page(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, back_Button_Damage_Detection_Sensitivity_Css)))
        self.driver.find_element_by_css_selector(back_Button_Damage_Detection_Sensitivity_Css).click()

    def click_refresh_button_threshold_page(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, refresh_Button_Damage_Detection_Sensitivity_Css)))
        self.driver.find_element_by_css_selector(refresh_Button_Damage_Detection_Sensitivity_Css).click()

    def click_closeup_sensitivity_button_threshold_page(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                    closeup_Sensitivity_Button_Damage_Detection_Sensitivity_Css)))
        self.driver.find_element_by_css_selector(closeup_Sensitivity_Button_Damage_Detection_Sensitivity_Css).click()

    def click_full_view_sensitivity_button_threshold_page(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                    full_View_Sensitivity_Button_Damage_Detection_Sensitivity_Css)))
        self.driver.find_element_by_css_selector(full_View_Sensitivity_Button_Damage_Detection_Sensitivity_Css).click()

    def get_threshold_option_text(self, index):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, sensitivity_Buttons_List_Css)))

        text = self.driver.find_elements_by_css_selector(sensitivity_Buttons_List_Css)[index].text
        return text

    def get_closeup_sensitivity_button_text_threshold_page(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                          closeup_Sensitivity_Button_Damage_Detection_Sensitivity_Css)))

        text = self.driver.find_element_by_css_selector(closeup_Sensitivity_Button_Damage_Detection_Sensitivity_Css)\
            .text
        return text

    def get_full_view_sensitivity_button_text_threshold_page(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                          full_View_Sensitivity_Button_Damage_Detection_Sensitivity_Css)))

        text = self.driver.find_element_by_css_selector(full_View_Sensitivity_Button_Damage_Detection_Sensitivity_Css)\
            .text
        return text

    def click_cancel_menu_button_threshold_page(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                    menu_Cancel_Button_Damage_Detection_Sensitivity_Css)))
        self.driver.find_element_by_css_selector(menu_Cancel_Button_Damage_Detection_Sensitivity_Css).click()

    def click_select_menu_button_threshold_page(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                    menu_Select_Button_Damage_Detection_Sensitivity_Css)))
        self.driver.find_element_by_css_selector(menu_Select_Button_Damage_Detection_Sensitivity_Css).click()

    def make_sure_menu_not_existed_threshold_page(self):
        try:
            self.wait.until(EC.invisibility_of_element((By.CSS_SELECTOR,
                                                              sensitivity_Buttons_List_Css)))
            return True
        except:
            return False

    def click_threshold_option(self, index):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, sensitivity_Buttons_List_Css)))

        text = self.driver.find_elements_by_css_selector(sensitivity_Buttons_List_Css)[index].click()
        return text
