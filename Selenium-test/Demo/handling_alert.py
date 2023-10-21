from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://demoqa.com/alerts")

driver.find_element(By.ID, "alertButton").click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(8)