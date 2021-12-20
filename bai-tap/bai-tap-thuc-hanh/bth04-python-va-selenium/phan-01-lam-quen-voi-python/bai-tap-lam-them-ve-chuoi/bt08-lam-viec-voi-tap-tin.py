# Đọc/mở và ghi tập tin

import os

class BaiTapVeTapTin:
    def bt08(self):
        thong_tin_can_ghi = "Tên: Thu"
        
        # Ghi tập tin
        tap_tin = open("bt08-lam-viec-voi-tap-tin.txt",
                       "a+", encoding="utf8")
        tap_tin.writelines(thong_tin_can_ghi)
        
        # Đọc tập tin
        tap_tin = open("bt08-lam-viec-voi-tap-tin.txt",
                       "r", encoding="utf8")
        
        # Đọc tất cả các dòng
        doc_tap_tin = tap_tin.read()
        
        print("Nội dung tập tin là: ")
        print(doc_tap_tin)

print("\n=====================================\n")

doc_ghi_tap_tin = BaiTapVeTapTin()
doc_ghi_tap_tin.bt08()

print("\n=====================================\n")