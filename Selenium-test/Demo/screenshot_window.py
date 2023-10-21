from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-logging'])
option.headless = True
#option argument jika full screen dengan ukuran layar
option.add_argument("--windows-size=1920,1080")


driver = webdriver.Chrome(options=option)
driver.get("https://demoqa.com")
print(driver.title)
driver.get_screenshot_as_file("Screenimage.png")