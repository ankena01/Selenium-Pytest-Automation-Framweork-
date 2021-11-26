# Locators of the search page + Page Actions
from base.base_driver import BaseDriver
from selenium.webdriver.common.by import By
import time
from utilities.utils import Utils
from testdata.test_data import Test_Data
import logging


class SearchFlightResults(BaseDriver):

    log = Utils.custom_logger(loglevel = logging.DEBUG)

####################Constructor #######################
    def __init__(self , driver ):
        self.driver = driver
        

    # Locators or Object Repository
    STOP_FIELD_1 = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    STOP_FIELD_2 = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    STOP_FIELD_0 = "//p[@class='font-lightgrey bold'][normalize-space()='0']"


    # Page Actions

    def filter_flights_by_1_stop(self):
        element = self.do_click(By.XPATH , self.STOP_FIELD_1)
        time.sleep(5)
        element.click()

        if len(Test_Data.test_data) > 1:
            self.driver.get("https://www.yatra.com/")
            self.driver.delete_all_cookies()
            self.driver.refresh()

        
            

    def filter_flights_by_2_stop(self):
        element = self.do_click(By.XPATH , self.STOP_FIELD_2)
        time.sleep(5)
        element.click()

        if len(Test_Data.test_data) > 1:
            self.driver.get("https://www.yatra.com/")
            self.driver.delete_all_cookies()
            self.driver.refresh()        

        

    def filter_flights_by_0_stop(self):
        element = self.do_click(By.XPATH , self.STOP_FIELD_0)
        time.sleep(5)
        element.click()

        if len(Test_Data.test_data) > 1:
            self.driver.get("https://www.yatra.com/")
            self.driver.delete_all_cookies()
            self.driver.refresh()        


        
    def filter_flights_by_stop(self, by_stop):
        if by_stop == "1 Stop":
            self.log.info("1 Stop is selected")
            self.filter_flights_by_1_stop()

        elif by_stop == "2 Stop":
            self.filter_flights_by_2_stop()
            self.log.info("2 Stop is selected")

        elif by_stop == "0 Stop":
            self.filter_flights_by_0_stop()
            self.log.info("0 Stop is selected")
        else:
            self.log.error("Please provide valid filter option!!!")

        
