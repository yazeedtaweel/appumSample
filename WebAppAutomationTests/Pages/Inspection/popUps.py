from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from Locators.InspectionPageLocators import *


class PopUps:
    # scan popup
    def click_yes_button_cancel_scan_popup(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, cancel_PopUp_yes_Button_CSS)))
        self.driver.find_element_by_css_selector(cancel_PopUp_yes_Button_CSS).click()

    def click_no_button_cancel_scan_popup(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, cancel_PopUp_no_Button_CSS)))
        self.driver.find_element_by_css_selector(cancel_PopUp_no_Button_CSS).click()

    def get_cancel_popup_message(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, cancel_PopUp_Message_Css)))
        return self.driver.find_element_by_css_selector(cancel_PopUp_Message_Css).text

    def make_sure_cancel_popup_is_closed(self):
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, cancel_PopUp_Message_Css)))
        return 1

    # skip popup
    def get_skip_popup_message(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, skip_PopUp_Message_CSS)))
        return self.driver.find_element_by_css_selector(skip_PopUp_Message_CSS).text

    def click_close_button_skip_popup(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, skip_PopUp_Close_Button_CSS)))
        self.driver.find_element_by_css_selector(skip_PopUp_Close_Button_CSS).click()

    def make_sure_skip_popup_is_closed(self):
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, skip_PopUp_Message_CSS)))
        return 1

    def fill_other_reason_skip_popup(self, text):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, other_Reason_Input_Css)))
        self.driver.find_element_by_css_selector(other_Reason_Input_Css).send_keys(text)

    # try again popup
    def get_failed_popup_message_body(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, failed_PopUp_Message_Body_Css)))
        return self.driver.find_element_by_css_selector(failed_PopUp_Message_Body_Css).text

    def get_failed_popup_message_title(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, failed_PopUp_Message_Title_Css)))
        return self.driver.find_element_by_css_selector(failed_PopUp_Message_Title_Css).text

    def click_try_again_button_failed_popup(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, failed_PopUp_TryAgain_Button_CSS)))
        self.driver.find_element_by_css_selector(failed_PopUp_TryAgain_Button_CSS).click()

    def click_dropdown_menu(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, skip_PopUp_Dropdown_Menu_Css)))
        self.driver.find_element_by_css_selector(skip_PopUp_Dropdown_Menu_Css).click()

    def select_dropdown_option(self, value):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, skip_PopUp_Dropdown_Menu_Css)))
        select = Select(self.driver.find_element_by_css_selector(skip_PopUp_Dropdown_Menu_Css))
        select.select_by_value(value)

    def click_go_on_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, skip_PopUp_Go_On_Button_CSS)))
        self.driver.find_element_by_css_selector(skip_PopUp_Go_On_Button_CSS).click()

    def check_popup_message(self, expected_message):
        # get image status message
        image_status_message = self.get_failed_popup_message_title()
        # compare it with the expected one
        try:
            assert expected_message == image_status_message, "status message is wrong"
        except Exception as e:
            raise
            print("error while getting message", format(e))

