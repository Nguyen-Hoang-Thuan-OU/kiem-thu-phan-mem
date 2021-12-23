# Trích xuất danh sách khoá học
# trên https://lms.ou.edu.vn/

# import json
import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select, WebDriverWait

# Ghi thông tin tài khoản và mật khẩu
# xuống tập tin CSV một cách tự động
# (tập tin CSV trùng với tên tập tin python)
with open('trich-xuat-danh-sach-khoa-hoc-tren-lms.ou.edu.vn.csv',
          'w', newline='') as f:
    ten_cot = ['tai_khoan', 'mat_khau']
    ghi_tap_tin = csv \
        .DictWriter(f,
                    fieldnames=ten_cot)
    ghi_tap_tin.writeheader()
    ghi_tap_tin.writerow({'tai_khoan': '1851xxxxxx',
                          'mat_khau': '**********'})

dich_vu = Service('venv/chromedriver.exe')
trinh_dieu_khien = webdriver.Chrome(service=dich_vu)

trinh_dieu_khien.get('https://lms.ou.edu.vn/')

# Cuộn xuống một đoạn
# trinh_dieu_khien\
#     .execute_script("window.scrollTo(0, 550)")
# time.sleep(1)

# Nhấn vào nút cuộn xuống
trinh_dieu_khien \
    .find_element(By.ID, 'scrollToAbout') \
    .click()

# Đợi một giây trước khi chọn học kỳ
time.sleep(1)

# Chọn học kỳ của hệ chính quy
trinh_dieu_khien \
    .find_element(By.CSS_SELECTOR, '#about a.main-btn') \
    .click()

# Chọn Đăng nhập bằng tài khoản HCMCOU-SSO
# để hiển thị biểu mẫu đăng nhập
trinh_dieu_khien \
    .find_element(By.CSS_SELECTOR, 'button.login100-form-btn') \
    .click()

# Chọn loại người dùng và nhập thông tin đăng nhập
#
# Vì đây là select box
# nên cần đặt khối lệnh bên trong Select
kieu_nguoi_dung = Select(trinh_dieu_khien
                         .find_element(By.ID, 'form-usertype'))
kieu_nguoi_dung.select_by_index(0)

# Đọc thông tin tài khoản và mật khẩu từ tập tin JSON
# with open('tap-tin-chua-tai-khoan-va-mat-khau.json') as f:
#     thong_tin_tai_khoan = json.load(f)
#     tai_khoan.send_keys(thong_tin_tai_khoan['tai_khoan'])
#     mat_khau.send_keys(thong_tin_tai_khoan['mat_khau'])

# Đọc thông tin tài khoản và mật khẩu
# từ tập tin CSV một cách tự động
with open('trich-xuat-danh-sach-khoa-hoc-tren-lms.ou.edu.vn.csv',
          'r', newline='') as f:
    doc_tap_tin = csv.DictReader(f)
    for doc_tung_dong in doc_tap_tin:
        doc_tai_khoan = doc_tung_dong['tai_khoan']
        doc_mat_khau = doc_tung_dong['mat_khau']

# Nhập thông tin tài khoản đã đọc được
# ở bên trong tập tin CSV
(trinh_dieu_khien
 .find_element(By.NAME,
               'form-username')) \
    .send_keys(doc_tai_khoan)

# Nhập thông tin mật khẩu đã đọc được
# ở bên trong tập tin CSV
(trinh_dieu_khien
 .find_element(By.NAME,
               'form-password')) \
    .send_keys(doc_mat_khau)

# Nhập thủ công thông tin tài khoản và mật khẩu
# tai_khoan = trinh_dieu_khien \
#     .find_element(By.ID, 'form-username')
# tai_khoan.send_keys('1851xxxxxx')
#
# mat_khau = trinh_dieu_khien \
#     .find_element(By.ID, 'form-password')
# mat_khau.send_keys('**********')

# Nhấn nút đăng nhập sau khi đã nhập thông tin
# "m-loginbox-submit-btn" là tên của class
trinh_dieu_khien \
    .find_element(By.CLASS_NAME, 'm-loginbox-submit-btn') \
    .click()

# Cuộn xuống một đoạn
# sau khi đã đăng nhập thành công
trinh_dieu_khien \
    .execute_script("window.scrollTo(0, 600)")

# Vì có lazy loading nên nếu muốn lấy
# danh sách tên của những khoá học
# phải chờ ngầm định (Implicit)
# hoặc chờ tường mình (Explicit)

# Chờ ngầm định (Implicit)
# trinh_dieu_khien.implicitly_wait(5)

# Chờ tường minh (Explicit)
WebDriverWait(trinh_dieu_khien, 30).until(
    ec.presence_of_all_elements_located((By.CSS_SELECTOR,
                                         '.dashboard-card')))

# Lấy danh sách tên của những khoá học
danh_sach_nhung_khoa_hoc = trinh_dieu_khien \
    .find_elements(By.CSS_SELECTOR,
                   '.dashboard-card .course-info-container .align-items-start a')

# Hiện tên của từng khoá học
print("\n=============CÁC KHOÁ HỌC=============\n")
for khoa_hoc in danh_sach_nhung_khoa_hoc:
    print(khoa_hoc.text)
    print("----------")

# trinh_dieu_khien.quit()
