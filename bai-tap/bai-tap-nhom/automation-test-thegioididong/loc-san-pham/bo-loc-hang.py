from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='venv\chromedriver.exe')
driver.get('https://www.thegioididong.com/')

def TestCase_Filter(driver,brand_name,cssSelector):
    # driver.find_element(By.CSS_SELECTOR, 'body header div.header__top div a.header__logo.theme-noel').click()
    # time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, 'body  header  div.header__main  div  ul  li:nth-child(1)  a').click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, 'body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-total div.filter-item__title.jsTitle').click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, cssSelector).click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, '#wrapper div.show-total-main div.filter-button.filter-button--total a.btn-filter-readmore').click()
    time.sleep(0.5)
    results = driver.find_elements(By.CSS_SELECTOR, '#categoryPage div.container-productbox ul li a.main-contain')
    for item in results:
        name = item.find_element(By.TAG_NAME, 'h3').text.lower()
        #print(name)
        if name.find(brand_name.lower()) == -1:
            return False
    return True
print("Case 7: pass - Reason: Tất cả sản phẩm hợp lệ với thương hiệu Iphone") if TestCase_Filter(driver,"iPhone",'#wrapper div.show-total-main div.show-total-item.clearfix.warpper-manu-inside.arranged div a:nth-child(1)') else print("Case 7: fail - Reason: Có sản phẩm không hợp lệ với thương hiệu Iphone")
print("Case 8: pass - Reason: Tất cả sản phẩm hợp lệ với thương hiệu Samsung") if TestCase_Filter(driver,"Samsung",'#wrapper div.show-total-main div.show-total-item.clearfix.warpper-manu-inside.arranged div a:nth-child(2)') else print("Case 8: fail - Reason: Có sản phẩm không hợp lệ với thương hiệu Samsung")
print("Case 9: pass - Reason: Tất cả sản phẩm hợp lệ với thương hiệu Oppo") if TestCase_Filter(driver,"Oppo",'#wrapper div.show-total-main div.show-total-item.clearfix.warpper-manu-inside.arranged div a:nth-child(3)') else print("Case 9: fail - Reason: Có sản phẩm không hợp lệ với thương hiệu Oppo")
print("Case 10: pass - Reason: Tất cả sản phẩm hợp lệ với thương hiệu Vivo") if TestCase_Filter(driver,"Vivo",'#wrapper div.show-total-main div.show-total-item.clearfix.warpper-manu-inside.arranged div a:nth-child(4)') else print("Case 10: fail - Reason: Có sản phẩm không hợp lệ với thương hiệu Vivo")
print("Case 11: pass - Reason: Tất cả sản phẩm hợp lệ với thương hiệu Xiaomi") if TestCase_Filter(driver,"Xiaomi",'#wrapper div.show-total-main div.show-total-item.clearfix.warpper-manu-inside.arranged div a:nth-child(5)') else print("Case 11: fail - Reason: Có sản phẩm không hợp lệ với thương hiệu Xiaomi")
print("Case 12: pass - Reason: Tất cả sản phẩm hợp lệ với thương hiệu Realme") if TestCase_Filter(driver,"Realme",'#wrapper  div.show-total-main  div.show-total-item.clearfix.warpper-manu-inside.arranged  div  a:nth-child(6)') else print("Case 12: fail - Reason: Có sản phẩm không hợp lệ với thương hiệu Realme")
print("Case 13: pass - Reason: Tất cả sản phẩm hợp lệ với thương hiệu Nokia") if TestCase_Filter(driver,"Nokia",'#wrapper div.show-total-main div.show-total-item.clearfix.warpper-manu-inside.arranged div a:nth-child(7)') else print("Case 13: fail - Reason: Có sản phẩm không hợp lệ với thương hiệu Nokia")
print("Case 14: pass - Reason: Tất cả sản phẩm hợp lệ với thương hiệu Mobell") if TestCase_Filter(driver,"Mobell",'#wrapper div.show-total-main div.show-total-item.clearfix.warpper-manu-inside.arranged div a:nth-child(8)') else print("Case 14: fail - Reason: Có sản phẩm không hợp lệ với thương hiệu Mobell")
print("Case 15: pass - Reason: Tất cả sản phẩm hợp lệ với thương hiệu Itel") if TestCase_Filter(driver,"Itel",'#wrapper div.show-total-main div.show-total-item.clearfix.warpper-manu-inside.arranged div a:nth-child(9)') else print("Case 15: fail - Reason: Có sản phẩm không hợp lệ với thương hiệu Itel")
print("Case 16: pass - Reason: Tất cả sản phẩm hợp lệ với thương hiệu Masstel") if TestCase_Filter(driver,"Masstel",'#wrapper div.show-total-main div.show-total-item.clearfix.warpper-manu-inside.arranged div a:nth-child(10)') else print("Case 16: fail - Reason: Có sản phẩm không hợp lệ với thương hiệu Masstel")
print("Case 17: pass - Reason: Tất cả sản phẩm hợp lệ với thương hiệu Energizer") if TestCase_Filter(driver,"Energizer",'#wrapper div.show-total-main div.show-total-item.clearfix.warpper-manu-inside.arranged div a:nth-child(11)') else print("Case 17: fail - Reason: Có sản phẩm không hợp lệ với thương hiệu Energizer")

