from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime
from selenium.webdriver.support.ui import Select

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
driver.find_element(By.XPATH,"//span[normalize-space()='JD']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[normalize-space()='Report']").click()
time.sleep(3)
dropdown = driver.find_element(By.XPATH,"//span[@id='select2-jd_list-container']")
dropdown.click()
time.sleep(2)

options = driver.find_elements(By.CSS_SELECTOR, "li.select2-results__option")
for option in options:
    if option.text.strip() == "JD-005 - saran_test":
        option.click()
        time.sleep(5)
        print(f"Dropdown list is verified: {option.text}")
        break
else:
    print("Desired option not found in the dropdown.")
