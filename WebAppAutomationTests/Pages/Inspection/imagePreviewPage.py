from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Locators.ImagePreviewPageLocators import *


class ImagePreview:

    def click_full_screen_preview_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, full_Screen_preview_Button_CSS)))
        self.driver.find_element_by_css_selector(full_Screen_preview_Button_CSS).click()

    def click_delete_preview_image_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, delete_Image_Button_CSS)))
        self.driver.find_element_by_css_selector(delete_Image_Button_CSS).click()

    def click_extra_closeup_preview_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, close_Preview_Button_CSS)))
        self.driver.find_element_by_css_selector(close_Preview_Button_CSS).click()

    def click_close_full_screen_preview_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, close_Full_Screen_Button_CSS)))
        self.driver.find_element_by_css_selector(close_Full_Screen_Button_CSS).click()

    def get_slider_previewed_images_count(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, preview_Images_Css)))
        images = self.driver.find_elements_by_css_selector(preview_Images_Css)
        return len(images)

    def get_extra_previewed_images_count(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, extra_Images_Previews_CSS)))
        images = self.driver.find_elements_by_css_selector(extra_Images_Previews_CSS)
        return len(images)

    def click_left_side_navigation_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, left_Side_Navigation_Button_Css)))
        self.driver.find_element_by_css_selector(left_Side_Navigation_Button_Css).click()

    def click_right_side_navigation_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, right_Side_Navigation_Button_Css)))
        self.driver.find_element_by_css_selector(right_Side_Navigation_Button_Css).click()

    def make_sure_left_side_navigation_button_invisible(self):
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, left_Side_Navigation_Button_Css)))
        return 1

    def make_sure_right_side_navigation_button_invisible(self):
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, right_Side_Navigation_Button_Css)))
        return 1

    def check_if_left_side_navigation_button_disabled(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, left_Side_Navigation_Button_Css)))
        return self.driver.find_element_by_css_selector(left_Side_Navigation_Button_Css).get_attribute("class")\
            .__contains__('slick-disabled')

    def check_if_right_side_navigation_button_disabled(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, right_Side_Navigation_Button_Css)))
        return self.driver.find_element_by_css_selector(right_Side_Navigation_Button_Css).get_attribute("class").\
            __contains__('slick-disabled')
