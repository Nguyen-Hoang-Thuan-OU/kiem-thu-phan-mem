'''
Viết một chương trình chấp nhận đầu vào là một câu,
đếm số chữ cái và chữ số trong câu đó.

Giả sử đầu vào sau được cấp cho chương trình: hello world! 123
Thì đầu ra sẽ là:
    Số chữ cái là: 10
    Số chữ số là: 3
'''

class BaiTapVeChuoi:
    def bt04(self):
        
        # Khởi tạo biến đếm
        dem_so = 0
        dem_chu = 0
        
        chuoi_nhap_vao =\
            input("Nhập vào danh sách chuỗi và phân tách nhau bởi dấu phẩy: ")
        
        # Duyệt chuỗi nhập vào và tăng biến đếm
        for i in chuoi_nhap_vao:
            if i.isdigit():
                dem_so = dem_so + 1
            elif i.isalpha():
                dem_chu = dem_chu + 1

        print()
        print("Chuỗi gốc là:", chuoi_nhap_vao)
        print()
        print("Số chữ cái là:", dem_chu)
        print("Số chữ số là:", dem_so)
                
print("\n=====================================\n")

dem_chu_cai_va_chu_so = BaiTapVeChuoi()
dem_chu_cai_va_chu_so.bt04()

print("\n=====================================\n")