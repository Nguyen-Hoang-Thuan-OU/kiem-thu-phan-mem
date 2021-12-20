'''
Chương trình để tạo ra một dictionary
chứa (i, i*i) như là số nguyên từ 1 đến n
(bao gồm cả 1 và n)

Giả sử số n là 8 thì đầu ra sẽ là:
{1: 1, 2: 4, 3: 9, 4:  16, 5: 25, 6: 36, 7: 49, 8: 64}
'''

class BaiTapVeDanhSach:
    def bt01(self):
        so_nguyen_n = int(input("Nhập vào số nguyên n: "))
        
        danh_sach = dict()
        for i in range(1, so_nguyen_n + 1):
            danh_sach[i] = i * i
        print(danh_sach)

print("\n=====================================\n")

danh_sach_tu_dien = BaiTapVeDanhSach()
danh_sach_tu_dien.bt01()

print("\n=====================================\n")