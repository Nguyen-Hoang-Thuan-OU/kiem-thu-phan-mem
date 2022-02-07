import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


path ="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)


def testMuaTraGop(kw):

    driver.get("https://www.thegioididong.com/tra-gop")
    tp = WebDriverWait(driver, 7).until(ec.presence_of_element_located((By.ID, "txtsuggest")))
    tp.send_keys(kw)
    time.sleep(5)
    l = driver.find_element(By.XPATH, './/*[@id="listsuggest"]')
    driver.implicitly_wait(5)

    list = l.find_elements(By.TAG_NAME, "li")
    if len(list) == 1:
        print("Không tồn tại sản phẩm")
        driver.close()
        return
    list[0].click()
    lmonth = driver.find_element(By.CLASS_NAME, "listmonths")
    listMonth = lmonth.find_elements(By.TAG_NAME, "li")
    h = 0
    lastResult = []
    for month in listMonth:
        title = "======================================== {0} ==========================================\n". format(month.text)
        print(title)
        m = month.find_element(By.TAG_NAME, "a")

        if h != 0:
            driver.execute_script("arguments[0].click();", m)
            time.sleep(8)
        lastResult.append( title + " " +OneMonth(int((month.text).split(" ")[0])))
        h = 1
    for last in lastResult:
        print(last)


def OneMonth(SoThang):
    time.sleep(8)
    driver.find_element(By.ID, "prepaid").click()
    infos = driver.find_element(By.CSS_SELECTOR, "ul.infolist")
    info = infos.find_elements(By.TAG_NAME,"li")
    del info[0:2]
    FinallyResult = []
    for i in range(0, len(info)+1):
        if (i != 0):
            time.sleep(15)
            driver.find_element(By.ID, "prepaid").click()
        time.sleep(5)
        s1 = str(i + 2)
        driver.find_element(By.XPATH, './/*[@id="listpercent"]/ul/li[' + s1 + ']').click()

        time.sleep(2)
        k = driver.find_element(By.ID,"prepaid").text
        FinallyResult.append( k + " " + str(OneTable(SoThang)))

        #for vv in FinallyResult:
          #  print(vv)
        time.sleep(5)
    stri = ""
    for i in FinallyResult:
        print(i)
        stri = stri + i + "\n"
    return stri



def OneTable(SoThang):


    ListResult = []
    time.sleep(12)
    listDict = []
    ListRow = driver.find_elements(By.CSS_SELECTOR,"ul.table>li")[2:]
    ListGiaTraGop = ListRow[0].find_elements(By.TAG_NAME,"aside")[1:]

    # Lấy các giá trị của bảng Table lưu vào ListDIct tương ứng
    for Slnpp in range(0,len(ListGiaTraGop)):
        if ListGiaTraGop[Slnpp].text != "":
            newdict = {"STT": Slnpp, "GiaTraGop": ListGiaTraGop[Slnpp].text, "TraTruoc": "", "LaiSuat": "", "TongGop": "",
                       "Goc+Lai": "", "PhiThuHo": "", "BaoHiem": "", "TongTienPhaiTra": "", "ChenhLech": ""}
            listDict.append(newdict)
    if len(listDict) == 0:
        ListResult.append("Không tồn tại công ty nào cho trả góp")
        return ListResult
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".subtable .gop").click()
    time.sleep(5)
    ListGiaTraTruoc = ListRow[1].find_elements(By.TAG_NAME, "aside")[1:]
    ListLaiSuat = ListRow[2].find_elements(By.TAG_NAME, "aside")[1:]
    ListTongGop = ListRow[4].find_elements(By.TAG_NAME, "aside")[1:]
    ListGocLai = ListRow[4].find_elements(By.CSS_SELECTOR, "div.infodetail>div")
    ListTongTien = ListRow[5].find_elements(By.TAG_NAME, "aside")[1:]
    ListChenhLech = ListRow[6].find_elements(By.TAG_NAME, "aside")[1:]
    for tt in range(0, len(ListGiaTraTruoc)):
        for i in listDict:
            if i["STT"] == tt:
                i.update({"TraTruoc": ListGiaTraTruoc[tt].text})
                i.update({"LaiSuat": ListLaiSuat[tt].text})
                i.update({"TongGop": ListTongGop[tt].text})
                i.update({"Goc+Lai": ListGocLai[0].find_elements(By.TAG_NAME, "aside")[tt + 1].text})
                i.update({"PhiThuHo": ListGocLai[1].find_elements(By.TAG_NAME, "aside")[tt + 1].text})
                i.update({"BaoHiem": ListGocLai[2].find_elements(By.TAG_NAME, "aside")[tt + 1].text})
                i.update({"TongTienPhaiTra": ListTongTien[tt].text})
                i.update({"ChenhLech": ListChenhLech[tt].text})
                break



    # Tính toán so sánh các value của 1 Table
    for vt in range(0, len(listDict)):
        print("===================== CÔNG TY {0} ================================". format(vt+1))
        TraGop = int((listDict[vt]["GiaTraGop"])[0:len(listDict[vt]["GiaTraGop"]) - 1].replace('.', ''))
        TraTruocW = (listDict[vt]["TraTruoc"].split(" "))
        TraTruocW[1] = TraTruocW[1][1:len(TraTruocW[1]) - 2]
        TraTruocW[0] = int((TraTruocW[0])[:len(TraTruocW[0]) - 1].replace('.', ''))
        print("Trả trước trong web", TraTruocW[0])
        TraTruoc = int(TraGop * (float(TraTruocW[1]) / 100))  # phantram
        print("Trả Trươc tính được", TraTruoc)
        if TraTruocW[0] == TraTruoc:
            print("-----PASS-----")
        else:
            print("----FAIL------")
            ListResult.append("Công Ty {0} FAIL giá mua trả trước " .format(vt+1))
            continue


        LaiSuat = listDict[vt]["LaiSuat"].replace("%", "")
        if LaiSuat.find("/") != -1:
            LaiSuat = float(LaiSuat.split("/")[1]) / 100
        else:
            LaiSuat = float(LaiSuat)/100


        GocLaiW = int((listDict[vt]["Goc+Lai"])[0:len(listDict[vt]["Goc+Lai"]) - 1].replace('.', ''))
        print("Tiền Gốc Lãi Web :", GocLaiW)
        Goc = (TraGop - TraTruoc) / SoThang
        LaiW = GocLaiW - Goc
        Lai = (TraGop - TraTruoc) * LaiSuat
        print("Tiền gốc + Lãi tính được:", int(Goc + Lai))
        # Trang Web có dòng "Lưu ý: Số tiền thực tế có thể chênh lệch đến 10.000đ/tháng" nên em tính nếu trong khoảng này vẫn cho nó là hợp lệ
        if (Goc + Lai) - 10000 < GocLaiW < (Goc +Lai) + 10000:
            print("-----PASS-----")
        else:
            print("----FAIL------")
            ListResult.append("Công Ty {0} FAIL Tính Tiền Gốc + Lãi ".format(vt + 1))
            continue

        TongGopW = int((listDict[vt]["TongGop"])[0:len(listDict[vt]["TongGop"]) - 1].replace('.', ''))
        print("Tong Góp Web:", TongGopW)
        viTriPTH = (listDict[vt]["PhiThuHo"]).find("₫")
        PhiThuHoW = int((listDict[vt]["PhiThuHo"])[:viTriPTH].replace('.', ''))
        BaoHiemW = int((listDict[vt]["BaoHiem"])[0:len(listDict[vt]["BaoHiem"]) - 1])
        TongGop = GocLaiW + PhiThuHoW + BaoHiemW
        print("TongGop:", TongGop)
        if TongGopW == TongGop:
            print("-----PASS-----")
        else:
            print("----FAIL------")
            ListResult.append("Công Ty {0} FAIL Tính Tổng số tiền góp mỗi tháng  ".format(vt + 1))
            continue


        TongTienPhaiTraW = int(listDict[vt]["TongTienPhaiTra"][0:len(listDict[vt]["GiaTraGop"]) - 1].replace('.', ''))
        print("Tổng tiền phải trả Web: ", TongTienPhaiTraW)
        TongTienPhaiTra = TraTruoc + TongGopW * SoThang
        print("Tổng tiền phải trả:", TongTienPhaiTra)
        if TongTienPhaiTraW == TongTienPhaiTra:
            print("-----PASS-----")
        else:
            print("----FAIL------")
            ListResult.append("Công Ty {0} FAIL Tổng Tiền Phải Trả ".format(vt + 1))
            continue

        ChenhLechW = int(listDict[vt]["ChenhLech"][0:len(listDict[vt]["ChenhLech"]) - 1].replace('.', ''))
        print("Chenh Lech Web", ChenhLechW)
        ChenhLech = round((LaiW + PhiThuHoW + BaoHiemW) * SoThang, -1)
        print("Chenh Lech", ChenhLech)
        if ChenhLechW == ChenhLech:
            print("-----PASS-----")
        else:
            print("----FAIL------")
            ListResult.append("Công Ty {0} FAIL Tính Chênh Lệch ".format(vt + 1))
            continue
        ListResult.append("Công Ty {0} PASS".format(vt + 1))
    return ListResult


#Test Case chạy khá lâu cần sự kiên nhẫn >.< tầm 25p

s = input("Nhập Từ Khóa Sản Phẩm Muốn Tìm Để Mua Trả Góp: ")
#samsung galaxy tab s7
#wwww
#459893
testMuaTraGop(s)



