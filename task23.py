
# task 23: Using Python Selenium Automation and Action Chains 
# visit the URL https://jqueryui.com/droppable/ and do a Drag and Drop operation 
# of the White Rectangular Box into the Yellow Rectangular Box 

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class actionchains:
    #constructor
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    # to get the url
    def get(self,url):
        self.driver.get(url)
    
    # performs drag n drop operation
    def dragndrop(self):
        # to maximize the window
        self.driver.maximize_window()
        # creating an variablefor action chains
        actionChains=ActionChains(self.driver)
         # Switch to the iframe
        frame1=self.driver.find_element(By.CSS_SELECTOR,value="iframe.demo-frame")
        self.driver.switch_to.frame(frame1)
        # Wait for source and destination elements
        time.sleep(2)
        # Perform drag and drop
        source=self.driver.find_element(By.ID,value="draggable")
        destination=self.driver.find_element(By.ID,value="droppable")        
        actionChains.drag_and_drop(source,destination).perform()

obj=actionchains()
obj.get("https://jqueryui.com/droppable/")
obj.dragndrop()
time.sleep(4)
