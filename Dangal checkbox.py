from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime

driver=webdriver.Chrome()
url="http://34.225.34.54/stldemo/login"
driver.get(url)
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@class='text-muted']").click()

Find_page = driver.find_element(By.CSS_SELECTOR,"h5.text-primary")
assert Find_page.text == "Forgot Password"
print('The Proper page is navigate')
time.sleep(2)
driver.back()
time.sleep(2)

driver.find_element(By.XPATH,"//input[@id='username']").send_keys("stl0002")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Mahi@123")
time.sleep(2)
driver.find_element(By.XPATH,"//i[@id='password-icon']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[@id='login_btn']").click()
time.sleep(2)
sucess_page = driver.find_element(By.CSS_SELECTOR,"h3.card-title")
assert sucess_page.text == "TASKS"
print("The page sucessfully moved dashboard page")
driver.find_element(By.XPATH,"//span[@class='side-menu__label'][normalize-space()='Master']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[normalize-space()='Holidays']").click()
time.sleep(2)
check_boxs=driver.find_element(By.XPATH,"//input[@id='flexCheckCheckedadd']").click()
time.sleep(5)    
'''
check_box_click_count=0
for check_box in check_boxs:
    if check_box.is_selected():
        check_box_click_count +=1
print('check box selected')
total_count=1
if total_count==check_box_click_count:
     print("checkbox count is sucessfully")'''




