from Locators.InspectionPageLocators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from conftest import *


class DriverFunctionality:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, pageElementsTimeOut)

    # permissions
    def give_camera_permissions(self):
        self.driver.switch_to.context('NATIVE_APP')
        self.wait.until(EC.element_to_be_clickable((By.XPATH, camera_allow_button_browser_XPATH)))
        self.driver.find_element_by_xpath(camera_allow_button_browser_XPATH).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, camera_allow_button_app_XPATH)))
        self.driver.find_element_by_xpath(camera_allow_button_app_XPATH).click()
        self.driver.switch_to.context('CHROMIUM')

    def give_camera_permissions_samsung(self):
        self.driver.switch_to.context('NATIVE_APP')
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id=\"root\"]/div/header/div/div[4]/div[2]")))
        self.driver.find_element_by_xpath("//div[@id=\"root\"]/div/header/div/div[4]/div[2]").click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id=\"root\"]/div/header/div/div[3]/div[2]")))
        self.driver.find_element_by_xpath("//div[@id=\"root\"]/div/header/div/div[3]/div[2]").click()
        self.driver.switch_to.context('CHROMIUM')

    def click_back_button(self):
        self.driver.back()

    def go_to_url(self, url):
        self.driver.find_element_by_css_selector('body')
        self.driver.get(url)

    def go_to_another_app_then_back(self):
        self.driver.switch_to.context('NATIVE_APP')
        self.driver.switch_to.context('CHROMIUM')
        self.driver.start_activity("com.android.settings", "Settings")
        self.driver.start_activity("com.android.chrome", "org.chromium.chrome.browser.ChromeTabbedActivity")
        self.driver.switch_to.context('CHROMIUM')

    def lock_the_phone_then_unlock(self):
        self.driver.lock()
        self.driver.unlock()

    def refresh_page(self):
        self.driver.refresh()

    def make_sure_permission_popup_invisible(self):
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, upload_image_loader_CSS)))
