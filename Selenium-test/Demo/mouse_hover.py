from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option)
driver.get("https://demoqa.com/menu")
driver.implicitly_wait(10)

#handler cara 1
menu = driver.find_element(By.LINK_TEXT, "Main Item 2")
hover = ActionChains(driver=driver).move_to_element(menu)
hover.perform()

ActionChains(driver=driver).move_to_element((driver.find_element(By.LINK_TEXT, "Main Item 2"))).perform()