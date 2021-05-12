from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Locators.ReportPageLocators import *
from conftest import *


class ReportPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, pageElementsTimeOut)

    def get_report_title(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, report_title_CSS)))
        return self.driver.find_element_by_css_selector(report_title_CSS).text

    def check_detailed_image_title_existed(self, text):
        self.wait.until(EC.text_to_be_present_in_element((By.XPATH, f"//*[text()='{text}']"), text))

    def get_car_details_images_count(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, car_Detail_Images_CSS)))
        detailed_images = self.driver.find_elements_by_css_selector(car_Detail_Images_CSS)
        return len(detailed_images)

    def get_extra_images_count(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, extra_Images_Xpath)))
        detailed_images = self.driver.find_elements_by_xpath(extra_Images_Xpath)
        return len(detailed_images)

    def get_closeup_images_count(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, closeup_Images_Xpath)))
        detailed_images = self.driver.find_elements_by_xpath(closeup_Images_Xpath)
        return len(detailed_images)

    def click_on_back_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, report_Back_Button_Css)))
        self.driver.find_element_by_css_selector(report_Back_Button_Css).click()

    def get_car_full_sides_images_count(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, full_Side_Images_Xpath)))
        extra_previews_images = self.driver.find_elements_by_xpath(full_Side_Images_Xpath)
        return len(extra_previews_images)

    def get_extra_images_report_count(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, extra_Images_report_Xpath)))
        extra_previews_images = self.driver.find_elements_by_xpath(extra_Images_report_Xpath)
        return len(extra_previews_images)
