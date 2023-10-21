from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option)

driver.get("https://demoqa.com/droppable/")

driver.implicitly_wait(10)

elements = driver.find_element(By.ID, "draggable")
kotak = driver.find_element(By.ID, "droppable")

action =ActionChains(driver)

action.drag_and_drop(elements, kotak).perform()