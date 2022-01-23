from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='venv\chromedriver.exe')
driver.get('https://www.thegioididong.com/')

def TestCase_ROM(driver, cssSelector,keyword):
    # driver.find_element(By.CSS_SELECTOR, 'body header div.header__top div a.header__logo.theme-noel').click()
    # time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, 'body  header  div.header__main  div  ul  li:nth-child(1)  a').click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, 'body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div:nth-child(8) div.filter-item__title.jsTitle.noselecttext span').click()
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
            info_tele = driver.find_elements(By.CSS_SELECTOR,'body section.detail div.box_main div.box_right div.parameter ul li:nth-child(7)')
            for item in info_tele:
                rom_tele = item.find_element(By.TAG_NAME,'span').text.lower()
                #print(rom_tele)
            if rom_tele.find(keyword.lower()) == -1:
                return 0
    else:
        return -1
    return 1


result =TestCase_ROM(driver,"body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.isShowing div.filter-show div.filter-list.props a:nth-child(1)",'8 GB')
print("Case 33: pass - Reason: Tất cả sản phẩm đều hợp lệ với bộ nhớ trong là 8GB") if result == 1 else (print("Case 33: fail - Reason: Có sản phẩm không hợp lệ với bộ nhớ trong 8GB") if result == 0 else print("Case 33: pass - Reason: Không có sản phẩm có bộ nhớ trong 8GB"))
result =TestCase_ROM(driver,"body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.isShowing div.filter-show div.filter-list.props a:nth-child(2)",'16 GB')
print("Case 34: pass - Reason: Tất cả sản phẩm đều hợp lệ với bộ nhớ trong là 16GB") if result == 1 else (print("Case 34: fail - Reason: Có sản phẩm không hợp lệ với bộ nhớ trong 16GB") if result == 0 else print("Case 34: pass - Reason: Không có sản phẩm có bộ nhớ trong 16GB"))
result =TestCase_ROM(driver,"body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.isShowing div.filter-show div.filter-list.props a:nth-child(3)",'32 GB')
print("Case 35: pass - Reason: Tất cả sản phẩm đều hợp lệ với bộ nhớ trong là 32GB") if result == 1 else (print("Case 35: fail - Reason: Có sản phẩm không hợp lệ với bộ nhớ trong 32GB") if result == 0 else print("Case 35: pass - Reason: Không có sản phẩm có bộ nhớ trong 32GB"))
result =TestCase_ROM(driver,"body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.isShowing div.filter-show div.filter-list.props a:nth-child(4)",'64 GB')
print("Case 36: pass - Reason: Tất cả sản phẩm đều hợp lệ với bộ nhớ trong là 64GB") if result == 1 else (print("Case 36: fail - Reason: Có sản phẩm không hợp lệ với bộ nhớ trong 64GB") if result == 0 else print("Case 36: pass - Reason: Không có sản phẩm có bộ nhớ trong 64GB"))
result =TestCase_ROM(driver,"body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.isShowing div.filter-show div.filter-list.props a:nth-child(5)",'128 GB')
print("Case 37: pass - Reason: Tất cả sản phẩm đều hợp lệ với bộ nhớ trong là 128GB") if result == 1 else (print("Case 37: fail - Reason: Có sản phẩm không hợp lệ với bộ nhớ trong 128GB") if result == 0 else print("Case 37: pass - Reason: Không có sản phẩm có bộ nhớ trong 128GB"))
result =TestCase_ROM(driver,"body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.isShowing div.filter-show div.filter-list.props a:nth-child(6)",'256 GB')
print("Case 38: pass - Reason: Tất cả sản phẩm đều hợp lệ với bộ nhớ trong là 256GB") if result == 1 else (print("Case 38: fail - Reason: Có sản phẩm không hợp lệ với bộ nhớ trong 256GB") if result == 0 else print("Case 38: pass - Reason: Không có sản phẩm có bộ nhớ trong 256GB"))
result =TestCase_ROM(driver,"body div.box-filter.top-box.block-scroll-main.cate-42 section div.jsfix.scrolling_inner.scroll-right div div.filter-item.isShowing div.filter-show div.filter-list.props a:nth-child(7)",'512 GB')
print("Case 39: pass - Reason: Tất cả sản phẩm đều hợp lệ với bộ nhớ trong là 512GB") if result == 1 else (print("Case 39: fail - Reason: Có sản phẩm không hợp lệ với bộ nhớ trong 512GB") if result == 0 else print("Case 39: pass - Reason: Không có sản phẩm có bộ nhớ trong 512GB"))