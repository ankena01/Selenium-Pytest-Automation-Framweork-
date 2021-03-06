from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from utilities.utils import Utils
import logging
import selenium

class BaseDriver:
    log = Utils.custom_logger(loglevel = logging.DEBUG)
    
    def __init__(self , driver):
        self.driver = driver

    def page_scroll(self):
        time.sleep(2)  # Allow 2 seconds for the web page to open
        scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
        screen_height = self.driver.execute_script("return window.screen.height;")   # get the screen height of the web
        i = 1

        while True:
            # scroll one screen height each time
            self.driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
            i += 1
            time.sleep(scroll_pause_time)
            # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
            scroll_height = self.driver.execute_script("return document.body.scrollHeight;")  
            # Break the loop when the height we need to scroll to is larger than the total scroll height
            if (screen_height) * i > scroll_height:
                break


    def do_click(self , locator_type , by_locator):

        element = WebDriverWait(self.driver , 30).until(ec.element_to_be_clickable((locator_type , by_locator)))
        return element
        

    def get_list_of_elements(self , locator_type , by_locator):
        elements = WebDriverWait(self.driver , 30).until(ec.visibility_of_any_elements_located((locator_type , by_locator)))
        return elements

# lines added by SDET 1

    
    def test_1_sdet_3(self):
        pass
        
    
