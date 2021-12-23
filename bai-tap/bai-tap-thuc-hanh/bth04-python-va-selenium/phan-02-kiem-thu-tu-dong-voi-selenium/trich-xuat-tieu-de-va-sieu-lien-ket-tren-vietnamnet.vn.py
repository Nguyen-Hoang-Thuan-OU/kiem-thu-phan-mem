# Trích xuất tiêu đề
# và siêu liên kết của các bài báo
# trên https://vietnamnet.vn/

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

dich_vu = Service('venv/chromedriver.exe')
trinh_dieu_khien = webdriver.Chrome(service=dich_vu)

trinh_dieu_khien.get('https://vietnamnet.vn/')

print("\n============TIÊU ĐỀ WEBSITE============\n")

print(trinh_dieu_khien.title)

print("\n===============TIÊU ĐỀ BÀI BÁO VÀ SIÊU LIÊN KẾT===============\n")

bai_bao_dau_tien = trinh_dieu_khien \
    .find_element(By.CSS_SELECTOR,
                  'div.TopNew div.clearfix a')

print("* Tiêu đề bài báo:", bai_bao_dau_tien.text)
print("---------------")
print("* Siêu liên kết:", bai_bao_dau_tien.get_attribute('href'))

print("\n===============================\n")

danh_sach_nhung_bai_bao_con_lai = trinh_dieu_khien \
    .find_elements(By.CSS_SELECTOR,
                   'div.TopNew ul.height-list a')

for bai_bao in danh_sach_nhung_bai_bao_con_lai:
    try:
        print("* Tiêu đề bài báo:", bai_bao.text)
        print("---------------")
        print("* Siêu liên kết:", bai_bao.get_attribute('href'))
        print("\n===============================\n")

    except NoSuchElementException:
        print("Đã xảy ra lỗi trong quá trình lấy phần tử!")
        print("\n===============================\n")
