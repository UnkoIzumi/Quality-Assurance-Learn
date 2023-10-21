from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

print("sample test case started")
#export PATH=$PATH:<dir>
driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.maximize_window()
# driver.switch_to.new_window('tab')

driver.get("https://opensource-demo.orangehrmlive.com/")

# Navigate to the website
# driver.get("https://qa-practice.netlify.app/bugs-form.html")

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")

driver.find_element(By.TAG_NAME, "button").send_keys(Keys.ENTER)

# Validate the title
expected_title = "OrangeHRM"
actual_title = driver.title #get to tittle website

#to get link current access
#print(driver .current_url)

if expected_title == actual_title:
    print("Title validation successful!")

else:
    print("Title validation failed. Expected:", expected_title, "Actual:", actual_title)

time.sleep(2)

driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--active']").send_keys("admin")
driver.find_element(By.XPATH, "//a[@class='oxd-main-menu-item']").click()
checking = driver.find_elements(By.XPATH, "//div[@class='oxd-table-card']")
value_checking = len(checking)
print(value_checking)

for data_check in range(1, (value_checking+1)):
    data_value = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div["+ str(data_check) +"]/div/div[2]/div").text
    print(data_value)
    
    if data_value == "Alice.Du":
        print("Found user in list")
        break
    elif data_check == value_checking:
        print("Cannot Find User Alice.Duval")

# assert data1 == "Alice.Duval", "Cannot Find User Alice.Duval"

time.sleep(3)
driver.close()

print("Successfully Testing")