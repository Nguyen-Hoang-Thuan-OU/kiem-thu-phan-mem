'''
Nhận chuỗi từ do người dùng nhập vào,
phân tách nhau bởi dấu phẩy
và in những từ đó thành chuỗi theo thứ tự bảng chữ cái,
phân tách nhau bằng dấu phẩy. 

Giả sử đầu vào được nhập là: without,hello,bag,world
thì đầu ra sẽ là: bag, hello, without, world
'''

class BaiTapVeChuoi:
    def bt03(self):
        chuoi_nhap_vao =\
            input("Nhập vào danh sách chuỗi và phân tách nhau bởi dấu phẩy: ")
            
        # Tách chuỗi khi gặp dấu phẩy
        tach_chuoi_khi_gap_dau_phay = \
            chuoi_nhap_vao.split(',')
        
        # Loại bỏ từ bị trùng lặp bằng set()
        loai_bo_tu_bi_trung_lap = sorted(set(tach_chuoi_khi_gap_dau_phay))
        
        print("Danh sách chuỗi sau khi đã được sắp xếp: " +
              ', '.join(loai_bo_tu_bi_trung_lap))
        
print("\n=====================================\n")

sap_xep_chuoi = BaiTapVeChuoi()
sap_xep_chuoi.bt03()

print("\n=====================================\n")