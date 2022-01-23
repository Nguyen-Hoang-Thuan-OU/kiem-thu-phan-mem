import time
from selenium import  webdriver
import  csv
from selenium.webdriver.common.by import By

driver = webdriver.Chrome( executable_path= 'C:\Program Files (x86)\chromedriver.exe')
driver.get('https://www.thegioididong.com/')

driver.find_element(By.XPATH,'/html/body/header/div[1]/div/div[3]/div[4]/a').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/section[1]/aside/div[2]/form/div/a').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/section[1]/div[1]/div/div/a[2]').click()
time.sleep(5)

driver.get('https://accounts.google.com/o/oauth2/auth/identifier?response_typ'
           'e=code&client_id=201330524028-473s01jufp3tq6ktjnjqghi3h7btt49h.apps.googleusercontent.com&redirect_'
           'uri=https%3A%2F%2Fwww.thegioididong.com%2Fhoi-dap%2Fauth%3FsocialType%3D2&scope=https%3A%2F%2Fwww.'
           'googleapis.com%2Fauth%2Fplus.me%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email%20https%3A%2F%2Fwww.'
           'googleapis.com%2Fauth%2Fuserinfo.profile&flowName=GeneralOAuthFlow')

with open('TaiKhoan.csv', newline='') as f:
    reader=csv.DictReader(f)
    for row in reader:
        m = row['mail']
        p=row['password']

(driver.find_element(By.ID,'identifierId')).send_keys(m)
time.sleep(2)

m = driver.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button/div[3]')
driver.execute_script("arguments[0].click();", m)
time.sleep(2)
(driver.find_element(By.NAME,'password')).send_keys(p)
time.sleep(2)
po = driver.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button/div[3]')
driver.execute_script("arguments[0].click();", po)
time.sleep(2)
driver.refresh()

driver.find_element(By.XPATH,'/html/body/section[1]/aside/div[2]/form/div/a').click()
time.sleep(2)

str = input("Nhap vao noi dung cau hoi cua ban: ")
inp = driver.find_element(By.ID,'txtContentQS')
inp.send_keys(str)

driver.find_element(By.XPATH,'/html/body/section[1]/aside/div[2]/div[2]/div/div[2]/button').click()
time.sleep(7)

driver.quit()
