from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def TestCase_Search(keyword, driver):
    #driver.find_element(By.CSS_SELECTOR, 'body header div.header__top div a.header__logo.theme-noel').click()
    inp = driver.find_element(By.ID, 'skw').send_keys(keyword)
    driver.find_element(By.CSS_SELECTOR, 'body header div.header__top div form button').click()
    results = driver.find_elements(By.CSS_SELECTOR, '#categoryPage div.container-productbox ul li a.main-contain')
    return len(results)


driver = webdriver.Chrome(executable_path='venv\chromedriver.exe')
driver.get('https://www.thegioididong.com/')
#CHỮ HOA
print("Case 1: pass - Reason: Có sản phẩm tồn tại ứng với keyword") if TestCase_Search("ĐIỆN THOẠI", driver) > 0 else print("Case 1: fail - Reason: Không có sản phẩm tồn tại ứng với keyword")
#chữ thường
print("Case 2: pass - Reason: Có sản phẩm tồn tại ứng với keyword") if TestCase_Search("điện thoại", driver) > 0 else print("Case 2: fail - Reason: Không có sản phẩm tồn tại ứng với keyword")
#Chữ hoa kết hợp chữ thường
print("Case 3: pass - Reason: Có sản phẩm tồn tại ứng với keyword") if TestCase_Search("Điện Thoại", driver) > 0 else print("Case 3: fail - Reason: Không có sản phẩm tồn tại ứng với keyword")
#Viết không dấu
print("Case 4: pass - Reason: Có sản phẩm tồn tại ứng với keyword") if TestCase_Search("dien thoai", driver) > 0 else print("Case 4: fail - Reason: Không có sản phẩm tồn tại ứng với keyword")
#Chữ viết tắt
print("Case 5: pass - Reason: Có sản phẩm tồn tại ứng với keyword") if TestCase_Search("dt", driver) > 0 else print("Case 5: fail - Reason: Không có sản phẩm tồn tại ứng với keyword")
#Chữ không có ý nghĩa
print("Case 6: pass - Reason: Không có sản phẩm tồn tại ứng với keyword") if TestCase_Search("XYZ ", driver) == 0 else print("Case 6: fail - Reason: Có sản phẩm tồn tại ứng với keyword")


driver.close()