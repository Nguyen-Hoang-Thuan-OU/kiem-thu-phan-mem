from selenium import  webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome( executable_path= 'C:\Program Files (x86)\chromedriver.exe')
driver.get('https://www.thegioididong.com/')

def TimDu_TinhHuyenXa():
    driver.find_element(By.XPATH,'/html/body/header/div[1]/div/a[2]').click()
    time.sleep(1)
    driver.find_element(By.ID, 'boxprovProvince').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="province-box"]/div/div/ul/li[43]/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="district-box-poup"]/div/div/ul/li[2]/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="ward-box"]/div/div/ul/li[3]/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="lc_btn-Confirm"]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,'/html/body/header/div[1]/div/a[2]').click()
    time.sleep(1)

TimDu_TinhHuyenXa()
driver.quit()
