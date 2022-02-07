from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='venv\chromedriver.exe')
driver.get('https://www.thegioididong.com/')

def TestCase_Price(driver, min, max, cssSelector):
    # driver.find_element(By.CSS_SELECTOR, 'body header div.header__top div a.header__logo.theme-noel').click()
    # time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, 'body  header  div.header__main  div  ul  li:nth-child(1)  a').click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, 'body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.warpper-price-outside div.filter-item__title.jsTitle span').click()
    time.sleep(0.5)
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, cssSelector).click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, 'body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.warpper-price-outside.isShowing div.filter-show div.filter-button a.btn-filter-readmore').click()
    time.sleep(0.5)
    results = driver.find_elements(By.CSS_SELECTOR, '#categoryPage div.container-productbox ul li a.main-contain')
    for item in results:
        price = (int)(item.find_element(By.CLASS_NAME, 'price').text.replace(".", "").replace("₫", ""))
        #print(price)
        if price >= max | price <= min:
            return False
    return True

print("Case 18: pass - Reason: Tất cả sản phẩm hợp lệ trong mức giá dưới 2 triệu") if TestCase_Price(driver,0, 2000000,'body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.warpper-price-outside.isShowing div.filter-show div.filter-list.price a:nth-child(1)') else print("Case 18: fail - Reason: Có sản phẩm không hợp lệ trong mức giá dưới 2 triệu")
print("Case 19: pass - Reason: Tất cả sản phẩm hợp lệ trong mức giá từ 2 đến 4 triệu") if TestCase_Price(driver,2000000, 4000000,'body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.warpper-price-outside.isShowing div.filter-show div.filter-list.price a:nth-child(2)') else print("Case 19: fail - Reason: Có sản phẩm không hợp lệ trong mức giá từ 2 đến 4 triệu")
print("Case 20: pass - Reason: Tất cả sản phẩm hợp lệ trong mức giá từ 4 đến 7 triệu") if TestCase_Price(driver,4000000, 7000000,'body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.warpper-price-outside.isShowing div.filter-show div.filter-list.price a:nth-child(3)') else print("Case 20: fail - Reason: Có sản phẩm không hợp lệ trong mức giá từ 4 đến 7 triệu")
print("Case 21: pass - Reason: Tất cả sản phẩm hợp lệ trong mức giá từ 7 đến 13 triệu") if TestCase_Price(driver,7000000, 13000000,'body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.warpper-price-outside.isShowing div.filter-show div.filter-list.price a:nth-child(4)') else print("Case 21: fail - Reason: Có sản phẩm không hợp lệ trong mức giá từ 7 đến 13 triệu")
print("Case 22: pass - Reason: Tất cả sản phẩm hợp lệ trong mức giá từ 13 đến 20 triệu") if TestCase_Price(driver,13000000, 20000000,'body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.warpper-price-outside.isShowing div.filter-show div.filter-list.price a:nth-child(5)') else print("Case 22: fail - Reason: Có sản phẩm không hợp lệ trong mức giá từ 13 đến 20 triệu")
print("Case 23: pass - Reason: Tất cả sản phẩm hợp lệ trong mức giá trên 20 triệu") if TestCase_Price(driver,20000000, 1000000000,'body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.warpper-price-outside.isShowing div.filter-show div.filter-list.price a:nth-child(6)') else print("Case 23: fail - Reason: Có sản phẩm không hợp lệ trong mức giá trên 20 triệu")
