from selenium import webdriver

option = webdriver.ChromeOptions()
option.headless = True

driver = webdriver.Chrome(options=option)
driver.get("https://demoqa.com")
print(driver.title)