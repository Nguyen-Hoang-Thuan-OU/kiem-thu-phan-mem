import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# region - Cấu hình cho webdriver
# Cài đặt tuỳ chỉnh cho Chrome
tuy_chinh = webdriver.ChromeOptions()

# Mặc định mở ở trong chế độ ẩn danh
tuy_chinh.add_argument("--incognito")

dinh_vu = Service('venv/chromedriver.exe')
trinh_dieu_khien = webdriver.Chrome(service=dinh_vu,
                                    options=tuy_chinh)
# endregion

# region - Trường hợp #1: Tiến hành đặt hàng nếu chưa có sản phẩm
trinh_dieu_khien.get("https://www.thegioididong.com/")
trinh_dieu_khien.set_window_size(1200, 720)

# Tắt thông báo hỏi địa chỉ giao hàng
# trong lần đầu truy cập website (nếu có)
try:
    vi_tri_thong_bao_dia_chi = trinh_dieu_khien \
        .find_element(By.XPATH,
                      """//*[@id="lc_pop--sugg"]/div/div[2]/a[2]""") \
        .click()
except:
    pass

o_tim_kiem = trinh_dieu_khien \
    .find_element(By.ID, "skw")

# Nhập thủ công sản phẩm cần tìm
# trong cửa sổ dòng lệnh trên PyCharm
# san_pham_can_tim = input("Nhập sản phẩm cần tìm: ")
# o_tim_kiem.send_keys(san_pham_can_tim)

# Gán cứng kết quả cần tìm
o_tim_kiem.send_keys("iPhone 13 Pro Max")

o_tim_kiem.submit()

# Dừng 1 giây sau khi nhấn tìm kiếm sản phẩm
# vì đây là giai đoạn chuyển trang
time.sleep(1)

# Định vị phần bao toàn bộ thuộc tính bên trong
san_phan_dau_tien_trong_tom_tat = trinh_dieu_khien \
    .find_element(By.XPATH,
                  """//h3[normalize-space()='iPhone 13 Pro Max 128GB']""") \
    .click()

# Dừng 1 giây vì đây là giai đoạn chuyển trang
time.sleep(1)

# Nhấn chọn lại dung lượng bộ nhớ trong
chon_bo_nho_trong = trinh_dieu_khien \
    .find_element(By.XPATH,
                  """//a[normalize-space()='128GB']""") \
    .click()

# Nhấn chọn màu sắc
chon_mau_sac = trinh_dieu_khien \
    .find_element(By.XPATH,
                  """//a[normalize-space()='Xám']""") \
    .click()

# Đợi hệ thống kiểm tra tình trạng còn hàng
# trinh_dieu_khien = WebDriverWait(trinh_dieu_khien, 10) \
#     .until(
#     ec.presence_of_all_elements_located((By.XPATH,
#                                          """//a[normalize-space()='MUA NGAY']"""))
# )

# Cuộn xuống 600 pixel
trinh_dieu_khien.execute_script("window.scrollTo(0, 600)")

# Đợi 2 giây khi tìm kiếm một phần tử
trinh_dieu_khien.implicitly_wait(2)

# Nhấn nút MUA NGAY
mua_ngay = trinh_dieu_khien \
    .find_element(By.XPATH,
                  """//a[normalize-space()='MUA NGAY']""") \
    .click()

# Đợi 2 giây khi tìm kiếm một phần tử
trinh_dieu_khien.implicitly_wait(2)

# Nhấn nút ĐẶT MUA/THÊM VÀO GIỎ HÀNG
them_vao_gio_hang = trinh_dieu_khien \
    .find_element(By.XPATH,
                  """//button[contains(text(),'Đặt mua')]""") \
    .click()

# Dừng 2 giây vì đây là giai đoạn chuyển trang
time.sleep(1)

# endregion

# region - Trường hợp #2: Truy cập vào giỏ hàng nếu đã có sản phẩm
trinh_dieu_khien.get("https://www.thegioididong.com/cart")
trinh_dieu_khien.set_window_size(1200, 720)

# Tắt thông báo hỏi địa chỉ giao hàng
# trong lần đầu truy cập website (nếu có)
try:
    vi_tri_thong_bao_dia_chi = trinh_dieu_khien \
        .find_element(By.XPATH,
                      """//*[@id="lc_pop--sugg"]/div/div[2]/a[2]""") \
        .click()
except:
    pass


# endregion

# region - TC_GioHang_009: Nhập tên khách hàng ĐÚNG
def nhap_ten_khach_hang_dung():
    # Nhập tên vào mục THÔNG TIN KHÁCH HÀNG 1
    trinh_dieu_khien \
        .find_element(By.XPATH,
                      """//input[@placeholder='Họ và Tên']""") \
        .send_keys("Trần An")
    time.sleep(2)
    trinh_dieu_khien.execute_script("window.scrollTo(0, 1000)")
    time.sleep(2)

    # Nhấn nút ĐẶT HÀNG 1
    trinh_dieu_khien \
        .find_element(By.XPATH,
                      """//button[@class='submitorder']""") \
        .click()

    # Xoá nội dung đã nhập cho KHÁCH HÀNG 1
    time.sleep(1)
    trinh_dieu_khien \
        .find_element(By.XPATH,
                      """//input[@placeholder='Họ và Tên']""") \
        .send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)

    # Nhập tên vào mục THÔNG TIN KHÁCH HÀNG 2
    trinh_dieu_khien \
        .find_element(By.XPATH,
                      """//input[@placeholder='Họ và Tên']""") \
        .send_keys("Trần.An")
    time.sleep(2)
    trinh_dieu_khien.execute_script("window.scrollTo(0, 1000)")
    time.sleep(2)

    # Nhấn nút ĐẶT HÀNG 2
    trinh_dieu_khien \
        .find_element(By.XPATH,
                      """//button[@class='submitorder']""") \
        .click()

    # Xoá nội dung đã nhập cho KHÁCH HÀNG 2
    time.sleep(1)
    trinh_dieu_khien \
        .find_element(By.XPATH,
                      """//input[@placeholder='Họ và Tên']""") \
        .send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)

    # Nhập tên vào mục THÔNG TIN KHÁCH HÀNG 3
    trinh_dieu_khien \
        .find_element(By.XPATH,
                      """//input[@placeholder='Họ và Tên']""") \
        .send_keys("Trần-An")
    time.sleep(2)
    trinh_dieu_khien.execute_script("window.scrollTo(0, 1000)")
    time.sleep(2)

    # Nhấn nút ĐẶT HÀNG 3
    trinh_dieu_khien \
        .find_element(By.XPATH,
                      """//button[@class='submitorder']""") \
        .click()

    if trinh_dieu_khien \
            .find_element(By.XPATH,
                          """//span[contains(text(),'Vui lòng nhập họ và tên')]""") is None:
        print("TC_GioHang_009 - PASSED")
    else:
        print("TC_GioHang_009 - FAILED")


# endregion

# region - TC_GioHang_010: Nhập tên khách hàng SAI
def nhap_ten_khach_hang_sai():
    # Nhập tên vào mục THÔNG TIN KHÁCH HÀNG 1
    trinh_dieu_khien \
        .find_element(By.XPATH,
                      """//input[@placeholder='Họ và Tên']""") \
        .send_keys("& An")
    time.sleep(2)
    trinh_dieu_khien.execute_script("window.scrollTo(0, 1000)")
    time.sleep(2)

    # Nhấn nút ĐẶT HÀNG 1
    trinh_dieu_khien \
        .find_element(By.XPATH,
                      """//button[@class='submitorder']""") \
        .click()

    # Xoá nội dung đã nhập cho KHÁCH HÀNG 1
    time.sleep(1)
    trinh_dieu_khien \
        .find_element(By.XPATH,
                      """//input[@placeholder='Họ và Tên']""") \
        .send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)

    # Nhập tên vào mục THÔNG TIN KHÁCH HÀNG 2
    trinh_dieu_khien \
        .find_element(By.XPATH,
                      """//input[@placeholder='Họ và Tên']""") \
        .send_keys("_ An")
    time.sleep(2)
    trinh_dieu_khien.execute_script("window.scrollTo(0, 1000)")
    time.sleep(2)

    # Nhấn nút ĐẶT HÀNG 2
    trinh_dieu_khien \
        .find_element(By.XPATH,
                      """//button[@class='submitorder']""") \
        .click()

    # Xoá nội dung đã nhập cho KHÁCH HÀNG 2
    time.sleep(1)
    trinh_dieu_khien \
        .find_element(By.XPATH,
                      """//input[@placeholder='Họ và Tên']""") \
        .send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)

    # Nhập tên vào mục THÔNG TIN KHÁCH HÀNG 3
    trinh_dieu_khien \
        .find_element(By.XPATH,
                      """//input[@placeholder='Họ và Tên']""") \
        .send_keys("................")
    time.sleep(2)
    trinh_dieu_khien.execute_script("window.scrollTo(0, 1000)")
    time.sleep(2)

    # Nhấn nút ĐẶT HÀNG 3
    trinh_dieu_khien \
        .find_element(By.XPATH,
                      """//button[@class='submitorder']""") \
        .click()


# endregion

# region - TC_GioHang_011: Nhập tên khách hàng bằng khoảng trắng
def nhap_ten_khach_hang_bang_khoang_trang():
    trinh_dieu_khien \
        .find_element(By.XPATH,
                      """//input[@placeholder='Họ và Tên']""") \
        .send_keys("          ")
    time.sleep(2)
    trinh_dieu_khien.execute_script("window.scrollTo(0, 1000)")
    time.sleep(2)


# endregion

# region - TC_GioHang_012: Nhập tên khách hàng bằng khoảng trắng
def nhap_ten_khach_hang_qua_so_luong_ky_tu_cho_phep():
    trinh_dieu_khien \
        .find_element(By.XPATH,
                      """//input[@placeholder='Họ và Tên']""") \
        .send_keys("25140552110144558292723115223549428345344505693192-123")
    time.sleep(2)
    trinh_dieu_khien.execute_script("window.scrollTo(0, 1000)")
    time.sleep(2)


# endregion

# region - Gọi hàm
print("\n================================================\n")

# Chạy TC_GioHang_009
# nhap_ten_khach_hang_dung()

print("\n================================================\n")

# Chạy TC_GioHang_010
# nhap_ten_khach_hang_sai()

print("\n================================================\n")

# Chạy TC_GioHang_011
# nhap_ten_khach_hang_bang_khoang_trang()

print("\n================================================\n")

# Chạy TC_GioHang_012
# nhap_ten_khach_hang_qua_so_luong_ky_tu_cho_phep()
# endregion
