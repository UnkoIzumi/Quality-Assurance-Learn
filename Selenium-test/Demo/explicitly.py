from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
revealed = driver.find_element(By.ID, "revealed")
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_selected)
        print('element telah dipencet')
    except TimeoutException:
        pass
