import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option)
driver.implicitly_wait(40)
#link 1
# driver.get("https://demoqa.com/upload-download/")
#link 2
driver.get("https://gofile.io/uploadFiles/")

#cara 1
# driver.find_element(By.ID, "uploadFile").send_keys("/home/miyaizu/Documents/Selenium-test/Browsers/LICENSE.chromedriver")

driver.find_element(By.XPATH, "//*[@id='filesUpload']/div/div[1]/div/button").send_keys(Keys.ENTER)

time.sleep(2)
pyautogui.click(193, 452)
time.sleep(2)
pyautogui.scroll(-30, 444, 484)
time.sleep(2)
pyautogui.click(353, 588)
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(343, 427)
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(460, 403)
pyautogui.press('enter')
