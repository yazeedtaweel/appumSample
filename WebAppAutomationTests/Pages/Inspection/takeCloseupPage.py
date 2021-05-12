from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Locators.ImagePreviewPageLocators import *


class TakeCloseupPage:

    def make_sure_original_image_preview_existed(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, original_Image_Preview_Css)))
        return 1

    def get_closeup_images_preview_count(self):
        elements = self.driver.find_elements_by_css_selector(closeup_Images_Previews_Css)
        return len(elements)

    def get_closeup_images_preview_closeup_screen_count(self):
        elements = self.driver.find_elements_by_css_selector(closeup_Images_Previews_Take_Closeup_Screen_Css)
        return len(elements)

    def click_closeup_preview_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, closeup_Images_Previews_Css)))
        self.driver.find_element_by_css_selector(closeup_Images_Previews_Css).click()
