'''
Viết một chương trình chấp nhận đầu vào là một câu,
đếm chữ hoa, chữ thường.

Giả sử đầu vào sau được cấp cho chương trình: PYTHON is Simple
Thì đầu ra sẽ là:
    Số chữ thường là: 7
    Số chữ hoa là: 7
'''

class BaiTapVeChuoi:
    def bt05(self):
        
        # Khởi tạo biến đếm
        dem_so_chu_thuong = 0
        dem_so_chu_hoa = 0
        
        chuoi_nhap_vao =\
            input("Nhập vào danh sách chuỗi và phân tách nhau bởi dấu phẩy: ")
        
        # Duyệt chuỗi nhập vào và tăng biến đếm
        for i in chuoi_nhap_vao:
            if i.islower():
                dem_so_chu_thuong = dem_so_chu_thuong + 1
            elif i.isupper():
                dem_so_chu_hoa = dem_so_chu_hoa + 1
             
        print()         
        print("Chuỗi gốc là:", chuoi_nhap_vao)
        print()
        print("Số chữ thường là:", dem_so_chu_thuong)
        print("Số chữ hoa là:", dem_so_chu_hoa)
                
print("\n=====================================\n")

dem_chu_thuong_va_chu_hoa = BaiTapVeChuoi()
dem_chu_thuong_va_chu_hoa.bt05()

print("\n=====================================\n")