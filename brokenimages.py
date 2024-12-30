import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


driver= webdriver.Chrome()
driver.get("http://34.225.34.54/stldemo/login")
driver.maximize_window()
images = driver.find_elements(By.TAG_NAME,"img")
print(f"The total number of images {len(images)}")
broken_images=[]

for demo in images:
    src = demo.get_attribute("src")
    resonse = requests.get(src)
    if resonse.status_code >200:
        broken_images.append(src)
        print('The broken images added')
    else:
        print("The broken images not added")
if broken_images:
    print("the broken images list is ")
    for broken_image in broken_images:
        print(f'the broken images{broken_image}')           