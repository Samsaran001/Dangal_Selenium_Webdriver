from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

driver=webdriver.Chrome()
url="http://34.225.34.54/stldemo/"
driver.get(url)
driver.maximize_window()
time.sleep(2)

username="stl0002"
password='Mahi@123'

driver.find_element(By.XPATH,"//input[@id='username']").send_keys(username)
driver.find_element(By.XPATH,"//input[@id='password']").send_keys(password)
time.sleep(2)
driver.find_element(By.XPATH,"//button[@id='login_btn']").click()
time.sleep(2)

all_links = driver.find_elements(By.TAG_NAME,'a')
print(f'total links count {len(all_links)}')
#Broken_links=[]

for demo in all_links:
    href = demo.get_attribute("href")
    if href and href.startswith(("http://", "https://")):
      try: 
        response=requests.get(href)
        if response.status_code >=400:
            print("The broken_link is found")
           #Broken_links.append(href)
            print(f'the href link name{href} and status_code is {response.status_code}')
        else:    
            print(f"server working is fine for {href}")
      except requests.exceptions.RequestException as e:
         print(f'error while requesting {href}:{e}')
    else:
       print("while skipping the program{href}")



              

