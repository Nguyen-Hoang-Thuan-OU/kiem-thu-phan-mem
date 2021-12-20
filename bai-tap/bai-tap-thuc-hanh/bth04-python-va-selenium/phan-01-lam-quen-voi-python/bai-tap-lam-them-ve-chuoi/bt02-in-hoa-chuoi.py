'''
Định nghĩa một class có ít nhất 2 method:
getString: để nhận một chuỗi do người dùng nhập vào
            từ giao diện điều khiển.
printString: in chuỗi vừa nhập sang chữ hoa.

Thêm vào các hàm hiểm tra đơn giản để kiểm tra method của class.

Ví dụ: Chuỗi nhập vào là dsaiou thì đầu ra phải là: DSAIOU
'''

class BaiTapVeChuoi:
    def bt02(self):
        chuoi_gia_tri = input("Nhập vào chuỗi giá trị: ")
        print("Chuỗi sau khi được in hoa: " + chuoi_gia_tri.upper())

print("\n=====================================\n")

chuyen_sang_chu_hoa = BaiTapVeChuoi()
chuyen_sang_chu_hoa.bt02()

print("\n=====================================\n")