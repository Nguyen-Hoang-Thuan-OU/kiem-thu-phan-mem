# Quản lý nhân viên ở một học viện

class bt04:
    
    # Khai báo danh sách (list) nhân viên
    danh_sach_nhan_vien = [
        {"ma_nv": 1, "ten_nv": "Nguyễn Văn A"},
        {"ma_nv": 2, "ten_nv": "Dương Trọng C"},
        {"ma_nv": 3, "ten_nv": "Nguyễn Thanh N"}
    ]
    n = len(danh_sach_nhan_vien)
    
    
    # Lấy toàn bộ danh sách nhân viên
    def lay_toan_bo_danh_sach_nhan_vien(self):
        for i in range(0, self.n):
            print("Mã nhân viên: {0}"
                  .format(self.danh_sach_nhan_vien[i]["ma_nv"]))
            print("Tên nhân viên: {0}"
                  .format(self.danh_sach_nhan_vien[i]["ten_nv"]))
            
    
    # Tìm kiếm nhân viên
    def tim_kiem_nhan_vien(self, ten_nhan_vien_can_tim):
        for i in range(0, self.n):
            if self.danh_sach_nhan_vien[i]["ten_nv"].find(ten_nhan_vien_can_tim) != -1:
                print("Mã nhân viên: {0}"
                  .format(self.danh_sach_nhan_vien[i]["ma_nv"]))
                print("Tên nhân viên: {0}"
                  .format(self.danh_sach_nhan_vien[i]["ten_nv"]))
                

    # Thêm mới nhân viên
    def them_moi_nhan_vien(self):
        id = int(input("Nhập mã nhân viên (số nguyên) cần thêm mới: "))
        
        # Kiểm tra nếu mã id đã tồn tại thì không thêm
        for i in range(0, self.n):
            if self.danh_sach_nhan_vien[i]["ma_nv"] == id:
                print("Mã nhân viên đã tồn tại, không thể thêm mới!")
                return -1
        
        # Nhập thông tin nhân viên cần thêm mới
        ten_nhan_vien_can_them = input("Nhập tên nhân viên cần thêm mới: ")
        nhan_vien_moi = {"ma_nv": id, "ten_nv": ten_nhan_vien_can_them}
        self.danh_sach_nhan_vien.append(nhan_vien_moi)
        
        # Cập nhật lại số lượng và in lại danh sách nhân viên
        print()
        self.n = len(self.danh_sach_nhan_vien)
        print("Danh sách nhân viên sau khi đã cập nhật: ")
        self.lay_toan_bo_danh_sach_nhan_vien()
        
        
    # Xoá nhân viên
    def xoa_nhan_vien_theo_ma_id(self, id):
        
        # Kiểm tra nhân viên có tồn tại, nếu có thì mới xoá
        for i in range(0, self.n):
            if self.danh_sach_nhan_vien[i]["ma_nv"] == id:
                del self.danh_sach_nhan_vien[i]
                
                # Cập nhật lại số lượng và in lại danh sách nhân viên
                print()
                self.n = len(self.danh_sach_nhan_vien)
                print("Danh sách nhân viên sau khi đã xoá: ")
                self.lay_toan_bo_danh_sach_nhan_vien()
                
                return
            
        # Nếu không tìm thấy nhân viên để xoá
        print("Nhân viên cần xoá không tồn tại!")
        
        
quan_ly_nhan_vien = bt04()

print("\n=======================================\n")

# Câu a: Hiển thị danh sách nhân viên
quan_ly_nhan_vien.lay_toan_bo_danh_sach_nhan_vien()

print("\n=======================================\n")

# Câu b: Nhập từ khoá cần tìm để tìm kiếm
ten_nhan_vien_can_tim = input("Nhập tên nhân viên cần tìm: ")
quan_ly_nhan_vien.tim_kiem_nhan_vien(ten_nhan_vien_can_tim)
 
print("\n=======================================\n")

# Câu c: Nhập từ khoá cần tìm để xoá
id_nhan_vien_can_xoa = int(input("Nhập mã nhân viên (số nguyên) cần xoá: "))
quan_ly_nhan_vien.xoa_nhan_vien_theo_ma_id(id_nhan_vien_can_xoa)

print("\n=======================================\n")

# Câu d: Nhập thông tin nhân viên để thêm mới
quan_ly_nhan_vien.them_moi_nhan_vien()

print("\n=======================================\n")
