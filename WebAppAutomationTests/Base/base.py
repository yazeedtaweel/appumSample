import os

import pytest
from appium import webdriver

from conftest import *


class Base:

    @pytest.fixture(autouse=True)
    def set_up(self):

        print("Initiating Appium driver")
        if os.environ['remote'].lower() == 'perfecto_android':
            self.driver = webdriver.Remote(Appium_URL_Perfecto, desired_cap_perfecto_android)
        elif os.environ['remote'].lower() == 'perfecto_ios':
            self.driver = webdriver.Remote(Appium_URL_Perfecto, desired_cap_perfecto_iphone)
        else:
            self.driver = webdriver.Remote(Appium_URL, desired_cap)

        # prepare the base url
        if os.environ['env'].lower() == 'qa':
            self.BaseUrl = qa_base_url
        else:
            self.BaseUrl = test_base_url

        # prepare the apiKey
        if os.environ['env'].lower() == 'qa':
            apiKey = 'f2f257d0-3d22-4b80-9194-df7435bdae02'
        else:
            apiKey = '12e920db-c826-44a2-b142-4b0d02ac6e7a'

        model_identifier = "00730-0014"
        client_process_id = "123456786"
        self.Url_WithCamera_WithEmail = f"{self.BaseUrl}?apikey={apiKey}&model_identifier={model_identifier}&client_process_id={client_process_id}"
        self.Url_NoCamera = f"{self.BaseUrl}?apikey={apiKey}&model_identifier={model_identifier}&client_process_id={client_process_id}&img_by_url=true"
        self.Url_NoCamera_NoEmail = f"{self.BaseUrl}?apikey={apiKey}&model_identifier={model_identifier}&client_process_id={client_process_id}&img_by_url=true&email=false"
        self.Url_NoCamera_WithEmail = f"{self.BaseUrl}?apikey={apiKey}&model_identifier={model_identifier}&client_process_id={client_process_id}&img_by_url=true&email=true"

        print("Test is started")
        self.driver.implicitly_wait(20)
        self.driver.orientation = "LANDSCAPE"
        self.driver.get(self.Url_NoCamera)

        yield self.driver
        if self.driver is not None:
            print("Tests is finished")
            self.driver.close()
            self.driver.quit()
