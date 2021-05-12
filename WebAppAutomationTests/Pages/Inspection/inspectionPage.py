import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Pages.Inspection.damageDetectionSensitivityPage import DamageDetectionSensitivity
from Pages.Inspection.imagePreviewPage import ImagePreview
from Pages.Inspection.takeCloseupPage import TakeCloseupPage
from conftest import *
from Locators.InspectionPageLocators import *
from Locators.ReportPageLocators import *
from Pages.Inspection.leftSideMenu import LeftSideMenu
from Pages.Inspection.popUps import PopUps
from Pages.Inspection.rightSideMenu import RightSideMenu
from Pages.Inspection.topTabs import TopTabs


class InspectionPage(LeftSideMenu, PopUps, RightSideMenu,
                     TopTabs, ImagePreview, TakeCloseupPage, DamageDetectionSensitivity):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, pageElementsTimeOut)

    def click_take_image_by_url_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, take_image_from_url_button_CSS)))
        self.driver.find_element_by_css_selector(take_image_from_url_button_CSS).click()

    def make_sure_take_image_by_url_exist(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, take_image_from_url_button_CSS)))
        return True

    def click_take_closeup_image_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, take_closeup_button_CSS)))
        self.driver.find_element_by_css_selector(take_closeup_button_CSS).click()

    def fill_image_url(self, image_url):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, image_url_input_CSS)))
        self.driver.find_element_by_css_selector(image_url_input_CSS).send_keys(image_url)

    def click_upload_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, upload_button_CSS)))
        self.driver.find_element_by_css_selector(upload_button_CSS).click()

    def wait_until_uploading_image(self):
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, upload_image_loader_CSS)))

    def get_status_message(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, status_message_CSS)))
        return self.driver.find_element_by_css_selector(status_message_CSS).text

    def click_back_from_closeup_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, back_from_close_up_CSS)))
        self.driver.find_element_by_css_selector(back_from_close_up_CSS).click()

    def click_done_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, done_button_CSS)))
        self.driver.find_element_by_css_selector(done_button_CSS).click()

    def get_report_title(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, report_title_CSS)))
        return self.driver.find_element_by_css_selector(report_title_CSS).text

    def get_canvas_width(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, canvas_CSS)))
        return self.driver.find_element_by_css_selector(canvas_CSS).value_of_css_property("width")

    def check_canvas_visibility(self):
        try:
            return self.driver.find_element_by_css_selector(canvas_CSS).is_displayed()
        except:
            return 0

    def check_background_image_visibility(self):
        try:
            return self.driver.find_element_by_css_selector(background_image_CSS).is_displayed()
        except:
            return 0

    def get_background_image_source(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, background_image_CSS)))
        return self.driver.find_element_by_css_selector(background_image_CSS).value_of_css_property("src")

    def upload_image(self, url):

        time.sleep(8)

        # click on update image by url button
        self.click_take_image_by_url_button()

        # fill the url field
        self.fill_image_url(url)

        time.sleep(4)

        # click on upload button
        self.click_upload_button()

    def upload_closeup_image(self, url, go_back=1):

        # click on take closeup button
        self.click_take_closeup_image_button()

        # click on take image from url button
        self.click_take_image_by_url_button()

        # fill the close up image url
        self.fill_image_url(url)

        # click on the upload image
        self.click_upload_button()

        if go_back == 1:
            # click back to the main view
            self.click_back_from_closeup_button()

    def make_sure_closeup_image_gone(self):
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, closeup_Image_Preview_Css)))

    def make_sure_extra_image_gone(self):
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, extra_Image_Preview_CSS)))

    def make_sure_extra_image_exist(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, extra_Image_Preview_CSS)))

    def click_delete_image_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, delete_image_CSS)))
        self.driver.find_element_by_css_selector(delete_image_CSS).click()

    def click_extra_image_preview(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, extra_Image_Preview_CSS)))
        self.driver.find_element_by_css_selector(extra_Image_Preview_CSS).click()

    def click_failed_message_close_button(self):
        self.driver.find_element_by_css_selector(failed_PopUp_Close_Button_CSS).click()

    def check_status_message(self, expected_message):
        # get image status message
        image_status_message = self.get_status_message()
        # compare it with the expected one
        try:
            assert expected_message == image_status_message, "status message is wrong"
        except Exception as e:
            raise
            print("error while getting message", format(e))

    def get_extra_images_previews_count(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, extra_Image_Preview_CSS)))
        extra_previews_images = self.driver.find_elements_by_css_selector(extra_Image_Preview_CSS)
        return len(extra_previews_images)