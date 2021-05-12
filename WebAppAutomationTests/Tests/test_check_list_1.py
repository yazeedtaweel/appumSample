import os

import allure
import pytest

from Base.base import Base
from Constants import *
from Helpers.driverFunctionality import DriverFunctionality
from Pages.Inspection.inspectionPage import InspectionPage
from Pages.createInspectionPage import CreateInspectionPage


@pytest.mark.usefixtures('set_up')
@allure.suite('Check list 1')
class TestCheckList1(Base):

    @allure.title('Test back button after start inspection text')
    @pytest.mark.skip
    @allure.severity("Medium")
    def test_case_009(self):

        # initiate drivers and pages
        driver = self.driver
        create_inspection_page = CreateInspectionPage(driver)

        driver_functionality = DriverFunctionality(driver)

        # click start inspection button
        create_inspection_page.click_start_inspection()

        # click on the back button
        driver_functionality.click_back_button()

        # make sure the start inspection page button exist
        is_displayed = create_inspection_page.check_start_inspection_button_visibility()

        try:
            assert 1 == is_displayed, "Start inspection button doesn't existed"
        except Exception as e:
            raise
            print("Start inspection button doesn't existed", format(e))

    @allure.title('Check camera permissions')
    @allure.severity("Medium")
    def test_case_010(self):

        # initiate drivers and pages
        driver = self.driver

        driver_functionality = DriverFunctionality(driver)

        driver_functionality.go_to_url(self.Url_WithCamera_WithEmail)

        # click inspection button
        create_inspection_page = CreateInspectionPage(driver)
        create_inspection_page.click_start_inspection()

        # go to the bae url
        if os.environ['remote'].lower() == 'perfecto_android':
            driver_functionality.give_camera_permissions_samsung()
        elif os.environ['remote'].lower() == 'windows':
            driver_functionality.give_camera_permissions()


        # refresh the page
        driver_functionality.refresh_page()

        # go to the main page
        driver_functionality.go_to_url(self.Url_WithCamera_WithEmail)

        # click inspection button
        create_inspection_page.click_start_inspection()

    @allure.title('Test all canvas for each side')
    @allure.severity("Medium")
    def test_case_012(self):

        # initiate drivers and pages
        driver = self.driver

        TestCheckList1.driver_functionality = DriverFunctionality(driver)

        self.driver_functionality.go_to_url(self.Url_WithCamera_WithEmail)

        # initiate the inspection page
        TestCheckList1.inspection_page = InspectionPage(driver)

        # click inspection button
        self.create_inspection_page = CreateInspectionPage(driver)
        self.create_inspection_page.click_start_inspection()

        # check give permissions
        if os.environ['remote'].lower() == 'perfecto_android':
            self.driver_functionality.give_camera_permissions_samsung()
        elif os.environ['remote'].lower() == 'windows':
            self.driver_functionality.give_camera_permissions()

        # check canvas for the front side
        self.check_canvas()

        # click on the right side
        self.inspection_page.click_right_button()

        # check canvas for the right side
        self.check_canvas()

        # click on the back side
        self.inspection_page.click_back_button()

        # check canvas for the back side
        self.check_canvas()

        # click on the left side
        self.inspection_page.click_left_button()

        # check canvas for the left
        self.check_canvas()

        # click on the extra side
        self.inspection_page.click_extras_button()

        # make sure the canvas is not loaded
        self.check_canvas(1)

    @allure.title('Test background image after inspect an image')
    @allure.severity("Medium")
    def test_case_013(self):

        # initiate drivers and pages
        driver = self.driver

        driver_functionality = DriverFunctionality(driver)

        driver_functionality.go_to_url(self.Url_WithCamera_WithEmail)

        # initiate the inspection page
        inspection_page = InspectionPage(driver)

        # click inspection button
        create_inspection_page = CreateInspectionPage(driver)
        create_inspection_page.click_start_inspection()

        # check give permissions
        if os.environ['remote'].lower() == 'perfecto_android':
            driver_functionality.give_camera_permissions_samsung()
        elif os.environ['remote'].lower() == 'windows':
            driver_functionality.give_camera_permissions()

        # click on the take image button
        inspection_page.click_take_photo_button()

        inspection_page.wait_until_uploading_image()

        background_image_displayed = inspection_page.check_background_image_visibility()

        try:
            assert background_image_displayed == 1, "background image does not displayed"
        except Exception as e:
            raise
            print("background image does not displayed", format(e))

    @allure.title('Test go to other app then back')
    @pytest.mark.skip
    @allure.severity("Medium")
    def test_case_014(self):

        # initiate drivers and pages
        driver = self.driver

        # click inspection button
        create_inspection_page = CreateInspectionPage(driver)

        # initiate the driver functionality
        driver_functionality = DriverFunctionality(driver)

        # go to settings and then back
        driver_functionality.go_to_another_app_then_back()

        # click start inspection
        create_inspection_page.click_start_inspection()

    @allure.title('Test lock the phone then take an image')
    @allure.severity("Medium")
    def test_case_015(self):

        # initiate drivers and pages
        driver = self.driver

        # click inspection button
        TestCheckList1.create_inspection_page = CreateInspectionPage(driver)

        # initiate the driver functionality
        TestCheckList1.driver_functionality = DriverFunctionality(driver)

        # initiate the inspection page
        TestCheckList1.inspection_page = InspectionPage(driver)

        # click on start inspection button
        self.create_inspection_page.click_start_inspection()

        # lock the phone and then unlock it
        self.driver_functionality.lock_the_phone_then_unlock()

        # upload the image - front
        self.inspection_page.upload_image(FrontSideImageWithDamageURL)

    def check_canvas(self, not_loaded=0):
        if not_loaded == 0:
            width_css = self.inspection_page.get_canvas_width()

            width = float(width_css[:len(width_css) - 3])

            try:
                assert 0 < width, "Canvas does not displayed"
            except Exception as e:
                raise
                print("Canvas does not displayed", format(e))
        else:
            is_canvas_visible = self.inspection_page.check_canvas_visibility()
            try:
                assert 0 == is_canvas_visible, "Canvas is visible"
            except Exception as e:
                raise
                print("Canvas is visible", format(e))
