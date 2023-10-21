from selenium import webdriver

driver = webdriver.Edge()
#ketika network/jaringan dalam kondisi jelek lemot, maka penggunaan implicity_wait untuk 
#menunggu si program untuk menemukan element yang telah dituju ( kondisi ini berlaku untuk semua element atau 1 project)
driver.implicitly_wait(10) #satuan detik
driver.get("https://google.com/")
