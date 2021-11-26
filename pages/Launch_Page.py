from base.base_driver import BaseDriver
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.search_flights_result_page import SearchFlightResults
from utilities.utils import Utils
import time
import logging

class LaunchPage(BaseDriver):

    # Locators or Object Repository

    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    ALL_CITIES = "//div[@class='viewport']//div[1]/li"
    DEPART_DATE_FIELD = "//input[@id='BE_flight_origin_date']"
    ARRIVAL_DATE_FIELD = "//input[@id='BE_flight_arrival_date']"
    ALL_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    SEARCH_FIELD = "#BE_flight_flsearch_btn[value='Search Flights']"


    # Constructor
    def __init__(self , driver):
        self.driver = driver
       

    # Page Actions

    # Departure Location
    def departfrom(self, depart_city):
        print(f"Departure location : {depart_city}")
        
        Utils.custom_logger(logging.DEBUG).info(f"Departure location : {depart_city}")

        #depart_from = self.wait.until(ec.element_to_be_clickable((By.XPATH , "//input[@id='BE_flight_origin_city']")))
        depart_from = self.do_click(By.XPATH , self.DEPART_FROM_FIELD)
        depart_from.click()
        depart_from.send_keys(depart_city)
        time.sleep(3)
        depart_from.send_keys(Keys.ENTER)


    # Arrival Location
    def going_to(self , arrival_city):
        #going_to = self.wait.until(ec.element_to_be_clickable((By.XPATH , "//input[@id='BE_flight_arrival_city']")))


        Utils.custom_logger(logging.DEBUG).critical(f"Arrival location : {arrival_city}")
        
        going_to = self.do_click(By.XPATH , self.GOING_TO_FIELD)
        going_to.click()
        going_to.send_keys(arrival_city)
        time.sleep(3)
        #search_results = self.wait.until(ec.visibility_of_any_elements_located((By.XPATH , "//div[@class='viewport']//div[1]/li")))
        
        
        search_results = self.get_list_of_elements(By.XPATH , self.ALL_CITIES)
        print("These are search results" , search_results)
        for result in search_results:
            if "New York (JFK)" in result.text:
                result.click()
                break

        
        #print("Total search results" , len(search_results))
        # for result in search_results:
        #     if "New York (JFK)" in result.text:
        #         result.click()
        #         break

    # Departure Date
    def select_departure_date(self, depart_date):
        #departure_date_field = self.wait.until(ec.element_to_be_clickable((By.XPATH , "//input[@id='BE_flight_origin_date']")))

        Utils.custom_logger(logging.DEBUG).critical(f"Departure date : {depart_date}")
        departure_date_field = self.do_click(By.XPATH , self.DEPART_DATE_FIELD)
        departure_date_field.click()
        #departure_date_field.send_keys(depart_date)
        #self.wait.until(ec.element_to_be_clickable((By.ID , depart_date))).click()
        self.do_click(By.ID , depart_date).click()


    # Select Arrival Date
    def select_return_date(self , return_date):
        #arrival_date_field = self.wait.until(ec.element_to_be_clickable((By.XPATH , "//input[@id='BE_flight_origin_date']")))

        Utils.custom_logger(logging.DEBUG).critical(f"Return date : {return_date}")
        arrival_date_field = self.do_click(By.XPATH , self.ARRIVAL_DATE_FIELD)
        arrival_date_field.click()
        #arrival_date = self.wait.until(ec.visibility_of_any_elements_located((By.XPATH , "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")))
        arrival_date = self.get_list_of_elements(By.XPATH , self.ALL_DATES)
        for date in arrival_date:
            if date.get_attribute("data-date") == return_date:
                date.click()
                break
    
    # Click on Search button
    def clicksearch(self):
        #self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR , "#BE_flight_flsearch_btn[value='Search Flights']"))).click()

        Utils.custom_logger(logging.DEBUG).critical(f"Search button clicked !!!")
        self.do_click(By.CSS_SELECTOR , self.SEARCH_FIELD).click()

    def search_flights(self , depart_city , arrival_city , depart_date , return_date):
        self.departfrom(depart_city)
        self.going_to(arrival_city)
        self.select_departure_date(depart_date)
        self.select_return_date(return_date)
        self.clicksearch()

        return SearchFlightResults(self.driver)






        


