# Tự động nhập thông tin và đăng ký tài khoản
# trên https://www.facebook.com/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Tuỳ chỉnh ngôn ngữ sang tiếng Anh
# vì có sử dụng XPATH
tuy_chinh = webdriver.ChromeOptions()
tuy_chinh.add_argument("--lang=en")

dich_vu = Service('venv/chromedriver.exe')
trinh_dieu_khien = webdriver.Chrome(service=dich_vu,
                                    options=tuy_chinh)

trinh_dieu_khien.get('https://www.facebook.com/')

try:
    # Đợi một giây
    trinh_dieu_khien.implicitly_wait(1)

    # Vì class và id của nút "Tạo tài khoản mới"
    # là loại tự động tạo nên sử dụng XPath
    # để lấy chuỗi trong nút: //*[text()='Create New Accout']
    trinh_dieu_khien \
        .find_element(By.XPATH,
                      "//*[text()='Create New Account']") \
        .click()

    # Nhập tên: Kiểm thử
    trinh_dieu_khien \
        .find_element(By.NAME, 'firstname') \
        .send_keys('Kiểm thử')

    # Nhập họ: Phần mềm
    trinh_dieu_khien \
        .find_element(By.NAME, 'lastname') \
        .send_keys('Phần mềm')

    # Nhập địa chỉ email: kiemthuphanmem@kiemthu.phanmem
    trinh_dieu_khien \
        .find_element(By.NAME, 'reg_email__') \
        .send_keys('kiemthuphanmem@kiemthu.phanmem')

    # Xác nhận lại địa chỉ email:
    # kiemthuphanmem@kiemthu.phanmem
    # (phần này sẽ bị ẩn cho đến khi nhập xong email)
    trinh_dieu_khien \
        .find_element(By.NAME, 'reg_email_confirmation__') \
        .send_keys('kiemthuphanmem@kiemthu.phanmem')

    # Nhập mật khẩu: KiemThuPhanMem!@#098
    trinh_dieu_khien \
        .find_element(By.NAME, 'reg_passwd__') \
        .send_keys('KiemThuPhanMem!@#098')

    # Nhập ngày sinh - select box
    ngay_sinh = Select(trinh_dieu_khien
                       .find_element(By.NAME,
                                     'birthday_day'))
    ngay_sinh.select_by_value('22')

    # Nhập tháng sinh - select box
    thang_sinh = Select(trinh_dieu_khien
                        .find_element(By.NAME,
                                      'birthday_month'))
    thang_sinh.select_by_value('12')

    # Nhập năm sinh - select box
    nam_sinh = Select(trinh_dieu_khien
                      .find_element(By.NAME,
                                    'birthday_year'))
    nam_sinh.select_by_value('2000')

    # Chọn giới tính, nhưng vì giới tính
    # là dạng radio button nên sử dụng XPath
    # để lấy chuỗi trong nút: //label[text()='Male']
    trinh_dieu_khien \
        .find_element(By.XPATH,
                      "//label[text()='Male']") \
        .click()

    # Nhấn nút đăng ký
    trinh_dieu_khien \
        .find_element(By.NAME,
                      'websubmit').click()

    print("\n===================================\n")
    print("Thao tác đăng ký đã hoàn tất!")
    print("\n===================================\n")

except Exception as ex:
    print("Đã xảy ra lỗi:", ex)

# trinh_dieu_khien.close()
