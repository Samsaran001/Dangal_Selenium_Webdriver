from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
url = "http://34.225.34.54/stldemo/login"
driver.get(url)
driver.maximize_window()

# Log in
driver.find_element(By.XPATH, "//input[@id='username']").send_keys("stl0002")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Mahi@123")
driver.find_element(By.XPATH, "//button[@id='login_btn']").click()

# Wait for Task Assignment menu item
try:
    task_assignment = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Task Assignment']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", task_assignment)
    task_assignment.click()
    print("Task Assignment clicked.")
except Exception as e:
    print("Error locating Task Assignment:", e)

# Wait for Assign Tasks
try:
    assign_tasks = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Assign Tasks']"))
    )
    assign_tasks.click()
    print("Assign Tasks clicked.")
except Exception as e:
    print("Error locating Assign Tasks:", e)

driver.quit()
