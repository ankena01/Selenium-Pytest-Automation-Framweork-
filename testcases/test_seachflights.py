# test cases
import logging
import pytest
from pages.Launch_Page import LaunchPage
from pages.search_flights_result_page import SearchFlightResults
from ddt import ddt , data , unpack , file_data
from utilities.utils import Utils
from testdata.test_data import Test_Data
from selenium.common.exceptions import ElementClickInterceptedException , TimeoutException

@pytest.mark.usefixtures("setup")
class BaseTest:
    pass

@pytest.mark.parametrize("depart_city , arrival_city , depart_date , return_date, stops" , Utils.read_data_from_json('./testdata/testdata.json'))    
class Test_Flights(BaseTest):

    @pytest.fixture(autouse=True)
    def example_setup(self):
        self.lp = LaunchPage(self.driver)
        #self.sf = SearchFlightResults(self.driver)
        


    # Page 1
    # @data([["New Delhi" , "New York" , "12/11/2021" , "13/11/2021" , "1 Stop"] , ["BOM" , "New York" , "12/11/2021" , "13/11/2021" , "2 Stop"]])
    # @unpack
    #@pytest.mark.parametrize("depart_city , arrival_city , depart_date , return_date, stops" , [["Pune" , "New York" , "12/11/2021" , "13/11/2021" , "0 Stop"]])    
    def test_1(self, depart_city , arrival_city , depart_date , return_date, stops):
        print("Depart city after apply ==> ", depart_city)
        
        # assert depart_city == "Pune"
        # assert stops == "0 Stop"
        # assert True == True


    

    #@pytest.mark.parametrize("depart_city , arrival_city , depart_date , return_date, stops" , Test_Data.test_data)
    #@pytest.mark.parametrize("depart_city , arrival_city , depart_date , return_date, stops" , [["New Delhi" , "New York" , "12/11/2021" , "13/11/2021","1 Stop"] ,["Mumbai" , "New York" , "12/11/2021" , "13/11/2021","2 Stop"]])
    
    def test_search_flights(self,depart_city , arrival_city , depart_date , return_date, stops):
        
        #lp = LaunchPage(self.driver)
        try:

            self.sf = self.lp.search_flights(depart_city , arrival_city , depart_date , return_date)
        
        except (TimeoutException , ElementClickInterceptedException,AttributeError) as e:
            Utils.custom_logger(loglevel = logging.DEBUG).exception(str(e))
        

    # Page 2

        #sf = SearchFlightResults(self.driver)
        self.lp.page_scroll()
        try:
            self.sf.filter_flights_by_stop(stops)

        except (TimeoutException , ElementClickInterceptedException,AttributeError) as e:
            Utils.custom_logger(loglevel = logging.DEBUG).exception(str(e))

        


