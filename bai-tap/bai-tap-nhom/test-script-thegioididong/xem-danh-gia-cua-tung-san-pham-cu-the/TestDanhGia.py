import time
import io
from selenium.common import exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def testDanhGia(SLSPMuonTest):
    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://www.thegioididong.com/")
    Phone = driver.find_element(By.CLASS_NAME, "box-common__main")
    ListPhone = Phone.find_elements(By.CSS_SELECTOR,".listproduct a")
    ListLink = []

    for i in ListPhone:
        ListLink.append(i.get_attribute("href"))
    sl = 0
    for l in ListLink[:SLSPMuonTest]:
        print("=====================================================================================================")
        driver.get(l)
        PhoneName = driver.find_element(By.CLASS_NAME, "detail ")
        PhoneName = PhoneName.find_element(By.TAG_NAME, "h1").text
        driver.execute_script("window.scrollTo(0,1000)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,1500)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,2500)")
        time.sleep(2)
        stt = 0
        PageNum = 0
        NumCmt = 0
        SLcmtTrenWeb =int( (driver.find_element(By.CLASS_NAME, "detail-rate-total").text).split(" ")[0])
        f = driver.find_elements(By.CSS_SELECTOR, ".box-border .comment-btn a") #Lấy vị trí button xem tất cả đánh giá
        if len(f) == 2:
            f[1].click()
            Page = driver.find_elements(By.CSS_SELECTOR, "div.pagcomment>a")
            if len(Page) > 0:
                Page = driver.find_elements(By.CSS_SELECTOR, "div.pagcomment>a")
                Page1 = len(Page) - 2
                Page = Page[Page1]
                PageNum = Page.get_attribute("title")
                PageNum = int(PageNum[6:])
        #chung
        try:
            cmt1 = WebDriverWait(driver, 7).until(ec.presence_of_all_elements_located((By.CLASS_NAME, "comment__item.par")))
        except:
            print("Không có cmt")
            break
        NumCmt = len(cmt1)
        time.sleep(3)
        for c in cmt1:
            stt = stt + 1
            print(stt)
            print(c.find_element(By.CLASS_NAME, "comment-content").text)
        #TH2
        for i in range(2,PageNum + 1): # Tong Page
                pn = "trang " + str(i)
                xp = "//a[@title='" + pn + "']"
                driver.find_element(By.XPATH, xp).click()
                time.sleep(2)
                cmt = WebDriverWait(driver,7).until(ec.presence_of_all_elements_located((By.CLASS_NAME,"comment__item.par")))
                NumCmt = NumCmt + len(cmt)
                for c in cmt: # 1 page
                    try:
                       stt = stt+1
                       print(stt)
                       print(c.find_element(By.CLASS_NAME,"comment-content").text)

                    except exceptions.StaleElementReferenceException as e:
                          print(c.find_element(By.CLASS_NAME,"comment-content").text)

        ghi = io.open("KetQuaSoLuongDG.txt", "a", encoding='utf-8')
        sl =  sl+1
        kq = "\n" + " " + str(sl)
        if NumCmt == SLcmtTrenWeb:
            kq = kq + " " + "\n{0}\nSố lượng đánh giá hiển thị {1}\nSố Lượng đánh giá đếm được:{2}    PASS". format(PhoneName,SLcmtTrenWeb,NumCmt)
            print(kq)
        else:
            kq = kq + " " + "\n {0}\nSố lượng đánh giá hiển thị {1}\nSố Lượng đánh giá đếm được:{2}    FAIL".format(PhoneName,SLcmtTrenWeb,NumCmt)
            print(kq)
        print("Link sản phẩm : ", l)

        ghi.writelines(kq)
        ghi.close()
    doc = open("KetQuaSoLuongDG.txt", encoding='utf-8')
    read = doc.read()
    doc.close()
    print(read)


n = int(input("Nhập số Sản Phẩm muốn test: "))
testDanhGia(n)
