import time
from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option)
driver.implicitly_wait(10)
driver.get("https://jqueryui.com/datepicker/")

driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='content']/iframe"))
#by click --->
# driver.find_element(By.ID, "datepicker").click()
# driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[6]/a").click()

#by specific change --->
driver.find_element(By.ID, "datepicker").send_keys('19/09/2023')
time.sleep(5)
driver.find_element(By.ID, "datepicker").clear()
