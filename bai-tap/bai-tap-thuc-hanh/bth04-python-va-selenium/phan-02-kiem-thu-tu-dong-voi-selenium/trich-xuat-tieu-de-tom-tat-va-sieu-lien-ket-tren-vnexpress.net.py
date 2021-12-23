# Trích xuất thông tin về tiêu đề,
# tóm tắt nội dung và siêu liên kết
# trên https://vnexpress.net/

# Sử dụng thư viện của một gói khác
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Tạo ra driver, trỏ đến vị trí của chromedriver
# đã được thêm vào môi trường ảo
dich_vu = Service('venv/chromedriver.exe')

# Chỉ định sử dụng trình duyệt Chrome
trinh_dieu_khien = webdriver.Chrome(service=dich_vu)

# Chỉ định website cần lấy thông tin
trinh_dieu_khien.get('https://vnexpress.net/')

print("\n============TIÊU ĐỀ WEBSITE============\n")

# Lấy thông tin tiêu đề
print(trinh_dieu_khien.title)

print("\n===============MÃ NGUỒN===============\n")

# Lấy mã nguồn
# print(trinh_dieu_khien.page_source)

print("\n========TIÊU ĐỀ BÀI BÁO, NỘI DUNG TÓM TẮT VÀ SIÊU LIÊN KẾT CỦA CÁC BÀI BÁO========\n")

# Lấy tiêu đề của những bài báo dựa trên css selector
#
# Sử dụng phương thức find_elements để nhận về
# danh sách các thành phần tìm thấy trong cây HTML DOM
#
# Sử dụng By để tìm thành phần HTML
# (Ví dụ: đi vào thẻ article -> lớp item-news)
danh_sach_nhung_bai_bao = trinh_dieu_khien \
    .find_elements(By.CSS_SELECTOR, 'article.item-news')

# Duyệt danh sách các bài báo,
# lấy tiêu đề, tóm tắt nội dung và siêu liên kết
for bai_bao in danh_sach_nhung_bai_bao:
    # Phương thức .find_element sẽ trả về
    # thành phần đầu tiên tìm thấy trong cây HTML DOM,
    # cần ném ngoại lệ NoSuchElementException
    # nếu không tìm thấy
    try:
        # Sử dụng .text để chỉ lấy nội dung
        tieu_de_bai_bao = bai_bao \
            .find_element(By.TAG_NAME, 'h3').text
        noi_dung_tom_tat_bai_bao = bai_bao \
            .find_element(By.TAG_NAME, 'p').text
        sieu_lien_ket_bai_bao = bai_bao \
            .find_element(By.CSS_SELECTOR,
                          'h3.title-news > a') \
            .get_attribute('href')

        print("* Tiêu đề bài báo:", tieu_de_bai_bao)
        print("---------------")
        print("* Nội dung tóm tắt:", noi_dung_tom_tat_bai_bao)
        print("---------------")
        print("* Siêu liên kết:", sieu_lien_ket_bai_bao)
        print("\n===============================\n")

    # Ném ra ngoại lệ nếu không tìm thấy thành phần
    except NoSuchElementException:
        print("Đã xảy ra lỗi trong quá trình lấy phần tử!")
        print("\n===============================\n")

print("\n======================================\n")

# Chỉ đóng trình duyệt
# trinh_dieu_khien.close()

# Đóng tất cả những thứ liên quan mà driver đã mở ra
# trinh_dieu_khien.quit()
