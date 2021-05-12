import allure
import pytest

from Base.base import Base
from Constants import FrontSideImageWithDamageURL, DamageDetectedMessage
from Pages.Inspection.inspectionPage import InspectionPage
from Pages.createInspectionPage import CreateInspectionPage
from Pages.reportPage import ReportPage


@pytest.mark.usefixtures('set_up')
@allure.suite('Inspection Page')
class TestSkipComponent(Base):

    @allure.title('Check the skip component')
    @allure.severity("Minor")
    def test_case_020(self):
        driver = self.driver

        # initiate the inspection page
        TestSkipComponent.inspection_page = InspectionPage(driver)

        # initiate the create inspection page
        create_inspection_page = CreateInspectionPage(driver)

        # initiate the report page
        TestSkipComponent.report_page = ReportPage(driver)

        # click inspection button
        create_inspection_page.click_start_inspection()

        # upload the image - front
        self.inspection_page.upload_image(FrontSideImageWithDamageURL)

        # check image status message
        self.inspection_page.check_status_message(DamageDetectedMessage)

        # check skip component - with side is blocked reason
        self.check_skip_component('1')

        # check skip component - with bad lighting reason
        self.check_skip_component('2')

        # check skip component - with other
        self.check_skip_component('4', 1, 'because of the test  purposes')

        # check skip component - with Phone camera fault reason
        self.check_skip_component('3')

    def check_skip_component(self, select_index, other=0, other_reason=""):
        # click skip button
        self.inspection_page.click_skip_button()

        # click dropdown menu
        self.inspection_page.click_dropdown_menu()

        # select the skip reason
        self.inspection_page.select_dropdown_option(select_index)

        # add test reason if it's other
        if other == 1:
            self.inspection_page.fill_other_reason_skip_popup(other_reason)

        # click dropdown menu
        self.inspection_page.click_dropdown_menu()

        # click go on button
        self.inspection_page.click_go_on_button()

        # check report title
        report_title = self.report_page.get_report_title()

        try:
            assert "Review Report" == report_title, "status message is wrong"
        except Exception as e:
            raise
            print("status message is wrong", format(e))

        # make sure the front image title existed
        self.report_page.check_detailed_image_title_existed("Front")

        # click on the back button from the report
        self.report_page.click_on_back_button()
