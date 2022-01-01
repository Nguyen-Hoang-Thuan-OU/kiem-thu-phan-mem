"""
Test case #01: tìm kiếm điện thoại,
trong kết quả tìm kiếm đầu tiên,
truy xuất và so sánh giá bán sau khi tìm kiếm
với giá bán sau khi đã chọn chi tiết sản phẩm

"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Cài đặt tuỳ chỉnh cho Chrome
tuy_chinh = webdriver.ChromeOptions()

# Mặc định mở ở trong chế độ ẩn danh
tuy_chinh.add_argument("--incognito")

dinh_vu = Service('venv/chromedriver.exe')
trinh_dieu_khien = webdriver.Chrome(service=dinh_vu,
                                    options=tuy_chinh)

trinh_dieu_khien.get("https://www.thegioididong.com/")

"""
Bước 00: Tắt thông báo chọn địa chỉ mua hàng
khi lần đầu truy cập vào website.
Vì đây là hyperlink nên phải sử dụng click()
"""
try:
    vi_tri_thong_bao_dia_chi = trinh_dieu_khien \
        .find_element(By.XPATH,
                      """//*[@id="lc_pop--sugg"]/div/div[2]/a[2]""") \
        .click()
except:
    pass

"""
Bước 01: Định vị ô tìm kiếm,
nhập từ khoá cần tìm và nhấn nút tìm kiếm.
Vì đây là form nên phải sử dụng submit()
"""
o_tim_kiem = trinh_dieu_khien \
    .find_element(By.ID, "skw")

o_tim_kiem.send_keys("iPhone 13")

o_tim_kiem.submit()

# Dừng 1 giây sau khi nhấn tìm kiếm sản phẩm
# vì đây là giai đoạn chuyển trang
time.sleep(1)

"""
Bước 02: Định vị giá của sản phẩm đầu tiên
trong danh sách kết quả trả về (phần tóm tắt)
bằng cách lấy thẻ <li> đầu tiên
"""
# Đinh vị phần bao toàn bộ thuộc tính bên trong
san_phan_dau_tien_trong_tom_tat = trinh_dieu_khien \
    .find_element(By.XPATH,
                  """//ul[@class='listsearch item2020 listproduct']//li[3]""")

# Lấy giá tiền của sản phẩm đầu tiên
# (đang giảm nếu có) ở kết quả tìm kiếm sản phẩm.
# Nhưng vì danh sách điện thoại tìm được rất nhiều
# nên cũng sẽ có rất nhiều thẻ có cùng class là price,
# thay vì tìm trên tổng thể thì ta sẽ tìm thẻ con
# ngay trong thẻ mà ta đang đứng, như thế sẽ giúp ta
# không bị lộn sang price của sản phẩm khác
gia_tien_cua_san_phan_dau_tien_trong_tom_tat = san_phan_dau_tien_trong_tom_tat \
    .find_element(By.CLASS_NAME, "price").text

print("Giá tiền trong tóm tắt:",
      gia_tien_cua_san_phan_dau_tien_trong_tom_tat,
      "(Đã bao gồm giá giảm)")

# Nhấn vào để xem chi tiết sản phẩm
# và lấy giá trong chi tiết sản phẩm để so sánh
san_phan_dau_tien_trong_tom_tat.click()

# Dừng 1 giây sau khi nhấn vào chi tiết sản phẩm
# vì đây là giai đoạn chuyển trang
time.sleep(1)

# Lấy giá tiền của sản phẩm đầu tiên (đang giảm)
# trong trang chi tiết sản phẩm.
# Lúc này đã chuyển sang trang mới
# nên phải tìm từ đầu bằng cách dùng trinh_dieu_khien
gia_tien_cua_san_phan_dau_tien_trong_chi_tiet = trinh_dieu_khien \
    .find_element(By.XPATH, """//p[@class='giamsoc-ol-price']""").text

print("Giá tiền trong chi tiết sản phẩm:",
      gia_tien_cua_san_phan_dau_tien_trong_chi_tiet,
      "(Đã bao gồm giá giảm)")

# Lấy giá tiền gốc của sản phẩm đầu tiên (không giảm)
# trong trang chi tiết sản phẩm.
# Lúc này đã chuyển sang trang mới
# nên phải tìm từ đầu bằng cách dùng trinh_dieu_khien
gia_tien_cua_san_phan_dau_tien_trong_chi_tiet = trinh_dieu_khien \
    .find_element(By.XPATH, """//p[@class='box-price-present black']""").text

print("Giá tiền gốc trong chi tiết sản phẩm:",
      gia_tien_cua_san_phan_dau_tien_trong_chi_tiet,
      "(Chưa bao gồm giá giảm)")
