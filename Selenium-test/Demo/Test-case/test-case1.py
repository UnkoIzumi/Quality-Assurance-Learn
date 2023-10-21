""" 
Test Case 1: Verify Internal and External Links in wikipedia.org

Test Steps:
1. Launch the Browser
2. Navigate to wikipedia.org selenium page
3. Click the “Create account” link
4. Capture the URL
5. Navigate back to Selenium Page
6. Click the “selenium.dev” link
7. Capture the URL
8. Close the Browser

Verification Point/s:
1. Verify if the 1st URL is an Internal link
2. Verify if the 2nd URL is an External link

Input Data/Test Data:
NA

Expected Result/URL:
1. https://en.wikipedia.org/wiki/Main_Page
2. http://www.seleniumhq.org


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

#link
url1 = "https://en.wikipedia.org/wiki/Main_Page"
url2 = "http://www.seleniumhq.org"

#URL website
driver.get(url1)

#getting current URL
get_url1 = driver.current_url
print(get_url1)

if get_url1 == url1:
    print('1st Verif: link passed')
else:
    print('1st Verif: link passed')

time.sleep(2)

#click create account
driver.find_element(By.ID, 'pt-createaccount-2').click()

#input username and password
driver.find_element(By.ID, 'wpName2').send_keys('Fahmi')
driver.find_element(By.ID, 'wpPassword2').send_keys('qwerty')
driver.find_element(By.ID, 'wpRetype').send_keys('qwerty')

#capture website
driver.get_screenshot_as_file("ScreenWikicreateaccount.png")

#navigate second link
driver.back()

# Open a new window 
driver.execute_script("window.open('');") 

# Switch to the new window and open new URL 
driver.switch_to.window(driver.window_handles[1]) 
driver.get(url2)

get_url2 = driver.current_url

if get_url2 == url2:
    print('2st Verif: link passed')
else:
    print('2st Verif: link passed')

#capture website
driver.get_screenshot_as_file("Screenshootexternallink.png")
cur_tab = len(driver.window_handles)

for handle in range(cur_tab):
    driver.switch_to.window(driver.window_handles[0])
    print("Close tab {}".format(handle))
    driver.close()