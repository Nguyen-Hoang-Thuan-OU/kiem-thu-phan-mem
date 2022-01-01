# Trích xuất kết quả tìm kiếm
# trên https://www.google.com/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

print('\n=================================\n')

# Nhập từ khoá tìm kiếm, ví dụ: kiểm thử phần mềm
tu_khoa_can_tim = input("Nhập từ khoá cần tìm: ")

print('\n=================================\n')

# Cài đặt tuỳ chỉnh cho Chrome
tuy_chinh = webdriver.ChromeOptions()

# Mặc định mở ở trong chế độ ẩn danh
tuy_chinh.add_argument("--incognito")

# Tuỳ chỉnh ngôn ngữ mặc định
tuy_chinh.add_argument("--lang=vi")

# Chỉ định Chrome Driver và trình duyệt sử dụng
dich_vu = Service('venv/chromedriver.exe')
trinh_dieu_khien = webdriver.Chrome(service=dich_vu,
                                    options=tuy_chinh)

# Chỉ định website
trinh_dieu_khien.get('https://www.google.com/')

# Sử dụng thuộc tính name có giá trị là q
gia_tri_nhap_vao = trinh_dieu_khien \
    .find_element(By.NAME, 'q')

# Lấy thông tin thuộc tính CSS của khung tìm kiếm:
# kích thước, kiểu chữ, màu chữ, màu nền,...
print("Thông tin thuộc tính CSS của ô tìm kiếm: ")
print("-----------")
print(gia_tri_nhap_vao
      .value_of_css_property('font-family'))

print(gia_tri_nhap_vao
      .value_of_css_property('color'))

print(gia_tri_nhap_vao
      .value_of_css_property('background-color'))

print(gia_tri_nhap_vao
      .value_of_css_property('width'))

print('\n=================================\n')

# Gửi giá trị dạng văn bản vào một ô nhập liệu
# hoặc nút bấm vào một control
gia_tri_nhap_vao.send_keys(tu_khoa_can_tim)
gia_tri_nhap_vao.submit()

danh_sach_cac_ket_qua_tim_kiem = trinh_dieu_khien \
    .find_elements(By.CSS_SELECTOR, 'div.g')
for ket_qua in danh_sach_cac_ket_qua_tim_kiem:
    noi_dung_tim_kiem = ket_qua \
        .find_element(By.TAG_NAME, 'a')
    print("* Tiêu đề:",
          noi_dung_tim_kiem.text)
    print("* Siêu liên kết:",
          noi_dung_tim_kiem.get_attribute('href'))
    print('\n=================================\n')

# Đóng trình duyệt sau khi lấy dữ liệu xong
trinh_dieu_khien.close()
