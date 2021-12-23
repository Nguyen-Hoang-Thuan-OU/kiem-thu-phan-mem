# Trích xuất tên sản phẩm, siêu liên kết
# và bình luận ở trang 1 của từng sản phẩm trên
# https://tiki.vn/dien-thoai-may-tinh-bang/c1789

import time
import uuid

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.common.exceptions import TimeoutException

dinh_vu = Service('venv/chromedriver.exe')
trinh_dieu_khien = webdriver.Chrome(service=dinh_vu)

trinh_dieu_khien.get('https://tiki.vn/dien-thoai-may-tinh-bang/c1789')

# Đưa trình duyệt vào chế độ toàn màn hình
trinh_dieu_khien.set_window_size(1920, 1080)
trinh_dieu_khien.maximize_window()

trinh_dieu_khien.execute_script("window.scrollTo(0, 500)")
time.sleep(1)
trinh_dieu_khien.execute_script("window.scrollTo(0, 1000)")
time.sleep(1)

danh_sach_san_pham = WebDriverWait(trinh_dieu_khien, 10) \
    .until(
    ec.presence_of_all_elements_located((By.CSS_SELECTOR,
                                         'a.product-item'))
)

print("\n=========DANH SÁCH SẢN PHẨM========\n")

# Khai báo danh sách để chứa các siêu liên kết
# của sản phẩm
danh_sach_sieu_lien_ket_cua_san_pham = []

for san_pham in danh_sach_san_pham[:3]:
    try:
        danh_sach_sieu_lien_ket_cua_san_pham \
            .append(san_pham.get_attribute('href'))

        # Lấy và in ra tên của sảm phẩm
        print(san_pham.find_element(By.CLASS_NAME,
                                    'name').text)
        print("\n------------------------------\n")
    except StaleElementReferenceException:
        pass

print("\n===========DANH SÁCH SIÊU LIÊN KẾT VÀ BÌNH LUẬN==========\n")

for lien_ket in danh_sach_sieu_lien_ket_cua_san_pham:
    print("\n~~~~~~~~~~Siêu liên kết~~~~~~~~~~\n")
    print(lien_ket)
    trinh_dieu_khien.get(lien_ket)

    # Cuộn xuống phần bình luận từ từ
    # vì có lazy loading
    trinh_dieu_khien.execute_script("window.scrollTo(0, 1000)")
    time.sleep(1)
    trinh_dieu_khien.execute_script("window.scrollTo(0, 2000)")
    time.sleep(1)
    trinh_dieu_khien.execute_script("window.scrollTo(0, 3000)")
    time.sleep(1)
    trinh_dieu_khien.execute_script("window.scrollTo(0, 4000)")

    try:
        # Đợi bình luận hiện ra,
        # sau năm giây nếu không hiện sẽ bỏ qua
        noi_dung_cac_binh_luan = WebDriverWait(trinh_dieu_khien, 5) \
            .until(
            ec.presence_of_all_elements_located((By.CLASS_NAME,
                                                 'review-comment__content'))
        )
        # In danh sách tất cả các bình luận ở trang 1 ra
        for binh_luan in noi_dung_cac_binh_luan:
            print("\n----------Bình luận của siêu liên kết bên trên----------\n")
            print(binh_luan.text)

        # Chụp màn hình sau khi lấy bình luận xong,
        # uuid.uuid4() dùng để tạo tên tự động cho ảnh
        trinh_dieu_khien.get_screenshot_as_file(str(uuid.uuid4()) + ".png")

    except TimeoutException:
        pass

print("\n==================================\n")

trinh_dieu_khien.close()
