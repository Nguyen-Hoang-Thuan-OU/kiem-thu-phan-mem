from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='venv\chromedriver.exe')
driver.get('https://www.thegioididong.com/')

def TestCase_RAM(driver, cssSelector,keyword):
    # driver.find_element(By.CSS_SELECTOR, 'body header div.header__top div a.header__logo.theme-noel').click()
    # time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, 'body  header  div.header__main  div  ul  li:nth-child(1)  a').click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, 'body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div:nth-child(7) div.filter-item__title.jsTitle.noselecttext span').click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, cssSelector).click()
    time.sleep(1)
    try:
        driver.find_element(By.CSS_SELECTOR, 'body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.isShowing div.filter-show div.filter-button a.btn-filter-readmore').click()
    except:
        driver.find_element(By.CSS_SELECTOR,'body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.isShowing div.filter-show div.filter-button a.btn-filter-close').click()
        return -1
    time.sleep(0.5)
    results = driver.find_elements(By.CSS_SELECTOR, '#categoryPage div.container-productbox ul li a.main-contain')
    if(len(results) != 0):
        list_link = []
        for item in results:
            link = item.get_attribute('href')
            list_link.append(link)
        for link in list_link:
            driver.get(link)
            info_tele = driver.find_elements(By.CSS_SELECTOR,'body section.detail div.box_main div.box_right div.parameter ul li:nth-child(6)')
            for item in info_tele:
                ram_tele = item.find_element(By.TAG_NAME,'span').text.lower()
                #print(ram_tele)
            if ram_tele.find(keyword.lower()) == -1:
                return 0
    else:
        return -1
    return 1

result =TestCase_RAM(driver,"body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.isShowing div.filter-show div.filter-list.props a:nth-child(1)",'1 GB')
print("Case 26: pass - Reason: Tất cả sản phẩm đều hợp lệ với ram 1GB") if result == 1 else (print("Case 26: fail - Reason: Có sản phẩm không phải ram 1GB") if result == 0 else print("Case 26: pass - Reason: Không có sản phẩm có ram 1GB"))
result =TestCase_RAM(driver,"body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.isShowing div.filter-show div.filter-list.props a:nth-child(2)",'2 GB')
print("Case 27: pass - Reason: Tất cả sản phẩm đều hợp lệ với ram 2GB") if result == 1 else (print("Case 27: fail - Reason: Có sản phẩm không phải ram 2GB") if result == 0 else print("Case 27: pass - Reason: Không có sản phẩm có ram 2GB"))
result =TestCase_RAM(driver,"body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.isShowing div.filter-show div.filter-list.props a:nth-child(3)",'3 GB')
print("Case 28: pass - Reason: Tất cả sản phẩm đều hợp lệ với ram 3GB") if result == 1 else (print("Case 28: fail - Reason: Có sản phẩm không phải ram 3GB") if result == 0 else print("Case 28: pass - Reason: Không có sản phẩm có ram 3GB"))
result =TestCase_RAM(driver,"body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.isShowing div.filter-show div.filter-list.props a:nth-child(4)",'4 GB')
print("Case 29: pass - Reason: Tất cả sản phẩm đều hợp lệ với ram 4GB") if result == 1 else (print("Case 29: fail - Reason: Có sản phẩm không phải ram 4GB") if result == 0 else print("Case 29: pass - Reason: Không có sản phẩm có ram 4GB"))
result =TestCase_RAM(driver,"body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.isShowing div.filter-show div.filter-list.props a:nth-child(5)",'6 GB')
print("Case 30: pass - Reason: Tất cả sản phẩm đều hợp lệ với ram 6GB") if result == 1 else (print("Case 30: fail - Reason: Có sản phẩm không phải ram 6GB") if result == 0 else print("Case 30: pass - Reason: Không có sản phẩm có ram 6GB"))
result =TestCase_RAM(driver,"body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.isShowing div.filter-show div.filter-list.props a:nth-child(6)",'8 GB')
print("Case 31: pass - Reason: Tất cả sản phẩm đều hợp lệ với ram 8GB") if result == 1 else (print("Case 31: fail - Reason: Có sản phẩm không phải ram 8GB") if result == 0 else print("Case 31: pass - Reason: Không có sản phẩm có ram 8GB"))
result =TestCase_RAM(driver,"body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.isShowing div.filter-show div.filter-list.props a:nth-child(7)",'12 GB')
print("Case 32: pass - Reason: Tất cả sản phẩm đều hợp lệ với ram 12GB") if result == 1 else (print("Case 32: fail - Reason: Có sản phẩm không phải ram 12GB") if result == 0 else print("Case 32: pass - Reason: Không có sản phẩm có ram 12GB"))