import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option)
driver.implicitly_wait(4)

for i in range(2):
    driver.get("https://tees.co.id/")

    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]")))
        print("pop up muncul")
        driver.find_element(By.CLASS_NAME, "btn-modal-close").click()
        
    except TimeoutException:
        print("pop up tidak muncul")
        pass

    time.sleep(3)