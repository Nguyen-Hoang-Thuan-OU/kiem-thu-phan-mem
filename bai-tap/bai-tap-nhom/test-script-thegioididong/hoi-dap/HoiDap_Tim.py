import time
from selenium import  webdriver
from selenium.webdriver.common.by import By

str = input("Nhap vao tu khoa can tim")

driver = webdriver.Chrome( executable_path= 'C:\Program Files (x86)\chromedriver.exe')
driver.get('https://www.thegioididong.com/')

driver.find_element(By.XPATH,'/html/body/header/div[1]/div/div[3]/div[4]/a').click()
time.sleep(2)
inp = driver.find_element(By.ID,'txtKeysearch')
inp.send_keys(str)
inp.submit()
time.sleep(2)
results = driver.find_elements(By.CSS_SELECTOR,'ul.listask')
for item in results:
    content = item.find_element(By.TAG_NAME,'a').text
    print(content)
    print('-----------------')

driver.close()
