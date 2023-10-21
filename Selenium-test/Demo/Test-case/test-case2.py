""" 

Test Case 2: Verify “Gmail” Link existence in Google Home page.

Test Steps:
1. Launch the Browser
2. Navigate to Google Home page (“https://www.google.com”)
3. Return the “Gmail” displayed status

Verification Point/s:
Verify the existence of “Gmail” Link
girt
Input Data:
NA

"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
option.add_experimental_option('excludeSwitches', ['enable-logging'])
#option argument jika full screen dengan ukuran layar
option.add_argument("--windows-size=1920,1080")

driver = webdriver.Chrome(options=option)
driver.implicitly_wait(10)

#Url
url = "https://www.google.com/"

driver.get(url)

try:
    link_extensi = driver.find_element(By.LINK_TEXT, "Gmail").is_displayed()
    
    if link_extensi == True:
        driver.find_element(By.PARTIAL_LINK_TEXT, "Gmail").click()
        print("Gmail Link - passed")
        get_url = driver.current_url
        print(get_url)
        
except:
    print("Gmail link - failed")
    get_url = driver.current_url
    print(get_url)
    pass

time.sleep(2)
driver.close()
