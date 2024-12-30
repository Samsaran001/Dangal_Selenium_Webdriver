from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime,timedelta
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url="http://34.225.34.54/stldemo/login"
chrome_option = Options()
chrome_option.add_argument("--disable-popup-blocking")
driver=webdriver.Chrome(chrome_option)
driver.get(url)
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@class='text-muted']").click()

actions=ActionChains(driver)
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
time.sleep(2)
driver.find_element(By.XPATH,"//span[contains(text(),'Leave')]").click()
time.sleep(4)
driver.find_element(By.XPATH,"//ul[@class='slide-menu open']//span[@class='sub-side-menu__label'][normalize-space()='Reports']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[normalize-space()='Leave Report']").click()
time.sleep(2)
leave_report_page=driver.find_element(By.CSS_SELECTOR,"h4.card-title.mb-0")
assert leave_report_page.text == "LEAVE REPORT"
print('The leave report page successfully moved')
time.sleep(2)
element = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='from_date_time']")))
driver.find_element(By.XPATH,"//input[@id='from_date_time']").click()
time.sleep(2)
calendar = driver.find_element(By.CLASS_NAME,"ui-datepicker-month")
assert calendar.text == "DECEMBER"
print('The calendar template ui is opened')
#current_date=datetime.now()
#next_date = current_date + timedelta(days=-2)
#format_date=next_date.strftime("%d%m%y")
#final=driver.find_element(By.XPATH,"//input[@id='from_date_time']").send_keys(format_date,Keys.TAB)
#print("calendar date select is complete")
driver.find_element(By.ID, "from_date_time").click()
From_date_picker = driver.find_element(By.ID, "from_date_time") 
driver.execute_script("arguments[0].value = '01-05-2023';", From_date_picker)
time.sleep(5)

driver.find_element(By.ID,"to_date_time").click()
To_date_picker = driver.find_element(By.ID,'to_date_time')
driver.execute_script("arguments[0].value = '24-12-2024' ;",To_date_picker)
time.sleep(3)

driver.find_element(By.XPATH,"//i[@class='fe fe-search btn btn-info']").click()
time.sleep(10)
driver.execute_script("window.scrollBy(0,100);")
time.sleep(5)
print('filter functionality is working')

'''
from_search = driver.find_element(By.CSS_SELECTOR,"//td[normalize-space()='Accounting']")
to_search= driver.find_element(By.XPATH,"//input[@class='form-control form-control']")

actions.drag_and_drop(from_search,to_search).perform()
time.sleep(5)
'''
driver.switch_to.new_window("http://34.225.34.54/stldemo/leave_request")
time.sleep(2)
print(f'Total handle of tabs',{len(driver.window_handles)})
Handle_tab_name=driver.window_handles
print(Handle_tab_name)
handle_current_name = driver.current_window_handle
print(handle_current_name)
