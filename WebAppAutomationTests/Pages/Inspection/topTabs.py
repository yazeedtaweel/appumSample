from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Locators.InspectionPageLocators import *


class TopTabs:

    def click_front_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, front_Button_CSS)))
        self.driver.find_element_by_css_selector(front_Button_CSS).click()

    def get_front_button_text(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, front_Button_CSS)))
        return self.driver.find_element_by_css_selector(front_Button_CSS).text

    def click_right_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, right_Button_CSS)))
        self.driver.find_element_by_css_selector(right_Button_CSS).click()

    def get_right_button_text(self):
        self.wait.until(EC.visibility_of((By.CSS_SELECTOR, right_Button_CSS)))
        self.driver.find_element_by_css_selector(right_Button_CSS).text

    def click_back_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, right_Button_CSS)))
        self.driver.find_element_by_css_selector(back_Button_CSS).click()

    def get_back_button_text(self):
        self.wait.until(EC.visibility_of((By.CSS_SELECTOR, back_Button_CSS)))
        self.driver.find_element_by_css_selector(back_Button_CSS).text

    def click_left_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, left_Button_CSS)))
        self.driver.find_element_by_css_selector(left_Button_CSS).click()

    def get_left_button_text(self):
        self.wait.until(EC.visibility_of((By.CSS_SELECTOR, left_Button_CSS)))
        self.driver.find_element_by_css_selector(left_Button_CSS).text

    def click_extras_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, extras_Button_CSS)))
        self.driver.find_element_by_css_selector(extras_Button_CSS).click()

    def get_extras_button_text(self):
        self.wait.until(EC.visibility_of((By.CSS_SELECTOR, extras_Button_CSS)))
        self.driver.find_element_by_css_selector(extras_Button_CSS).text

    def get_left_status_icon_color(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, left_Side_Status_Icon_Css)))
        return self.driver.find_element_by_css_selector(left_Side_Status_Icon_Css).value_of_css_property("fill")

    def get_right_status_icon_color(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, right_Side_Status_Icon_Css)))
        return self.driver.find_element_by_css_selector(right_Side_Status_Icon_Css).value_of_css_property("fill")

    def get_back_status_icon_color(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, back_Side_Status_Icon_Css)))
        return self.driver.find_element_by_css_selector(back_Side_Status_Icon_Css).value_of_css_property("fill")

    def get_front_status_icon_color(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, front_Side_Status_Icon_Css)))
        return self.driver.find_element_by_css_selector(front_Side_Status_Icon_Css).value_of_css_property("fill")

    def check_status_icon_color(self, side, expected_color):

        if side.value == 1:
            color = self.get_front_status_icon_color()
        elif side.value == 2:
            color = self.get_right_status_icon_color()
        elif side.value == 3:
            color = self.get_back_status_icon_color()
        elif side.value == 4:
            color = self.get_left_status_icon_color()
        else:
            raise print("status icon color is not as expected")

        try:
            assert expected_color == color, "status icon color is not as expected"
        except Exception as e:
            raise
            print("error while getting the status icon color", format(e))
