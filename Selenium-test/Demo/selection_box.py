from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option)
driver.implicitly_wait(10)

#selection method option
# driver.get("https://demoqa.com/select-menu/")
# pilih = Select(driver.find_element(By.ID, "oldSelectMenu"))
# pilih.select_by_value(10)

#selection new method
driver.get("https://www.google.com/maps/")
#first search place hotel
driver.find_element(By.ID, "searchboxinput").send_keys("Hilton London Bankside")
#click on the All reviews element to open up the dorpdown element
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='ydp1wd-haAclf']/div[5]"))).click()