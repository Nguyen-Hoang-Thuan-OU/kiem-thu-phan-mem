from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='venv\chromedriver.exe')
driver.get('https://www.thegioididong.com/')

def TestCase_Type(driver, cssSelector,keyword):
    # driver.find_element(By.CSS_SELECTOR, 'body header div.header__top div a.header__logo.theme-noel').click()
    # time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, 'body  header  div.header__main  div  ul  li:nth-child(1)  a').click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, 'body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div:nth-child(5) div.filter-item__title.jsTitle.noselecttext span').click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, cssSelector).click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.isShowing div.filter-show div.filter-button a.btn-filter-readmore').click()
    time.sleep(0.5)
    results = driver.find_elements(By.CSS_SELECTOR, '#categoryPage div.container-productbox ul li a.main-contain')
    list_link = []
    for item in results:
        link = item.get_attribute('href')
        list_link.append(link)
    for link in list_link:
        driver.get(link)
        info_tele = driver.find_elements(By.CSS_SELECTOR,'body section.detail div.box_main div.box_right div.parameter ul li:nth-child(2)')
        for item in info_tele:
            type_tele = item.find_element(By.TAG_NAME,'span').text.lower()
            #print(type_tele)
        if type_tele.find(keyword.lower()) == -1:
            return False
    return True

print("Case 24: pass - Reason: Tất cả sản phẩm hợp lệ với loại Android") if TestCase_Type(driver,"body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.isShowing div.filter-show div.filter-list.props a:nth-child(1)",'Android') else print("Case 24: fail - Reason: Có sản phẩm không hợp lệ với loại Android")
print("Case 25: pass - Reason: Tất cả sản phẩm hợp lệ với loại Iphone(iOS)") if TestCase_Type(driver,"body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.isShowing div.filter-show div.filter-list.props a:nth-child(2)",'iOS') else print("Case 25: fail - Reason: Có sản phẩm không hợp lệ với loại Iphone (iOS)")