# Viết chương trình thực hiện việc xử lý từ điển Anh – Việt

def tu_dien():
    danh_sach_tu_dien = {
        'tester': 'kiểm thử viên',
        'developer': 'lập trình viên',
        'project manager': 'quản lý dự án'
    }
    
    print("Danh sách từ điển hiện tại: ")
    print(danh_sach_tu_dien)

    # Câu a: Thêm từ mới vào từ điển
    danh_sach_tu_dien.update({'software testing': 'kiểm thử phần mềm'})
    danh_sach_tu_dien.update({'QA': 'kiểm soát chất lượng'})
        
    print("\n=======================================\n")
    
    # Câu b: Hiển thị từ điển và cho biết số phần tử hiện tại
    print("Danh sách từ điển sau khi đã được cập nhật: ")
    print(danh_sach_tu_dien)
    print()
    print("Số phần tử hiện tại trong từ điển: %d" %len(danh_sach_tu_dien))
            
    print("\n=======================================\n")
    
    # Câu c: Tìm kiếm từ tiếng Anh, thông báo nếu không tìm thấy
    gia_tri_can_tim = input("Nhập giá trị cần tìm (từ tiếng Anh): ")
    
    bien_co = 'false'
    for tu_khoa_trong_danh_sach in danh_sach_tu_dien.keys():
        if tu_khoa_trong_danh_sach == gia_tri_can_tim:
            bien_co = 'true'
            break
        
    print()
    if bien_co == 'false':
        print("Không tìm thấy từ cần tìm!")
    else:
        print("Đã tìm thấy từ!")
        print(gia_tri_can_tim + " = " + danh_sach_tu_dien[gia_tri_can_tim])
            
    print("\n=======================================\n")
    
    # Câu d: Xoá một từ trong từ điển dựa theo key
    gia_tri_can_xoa = input("Nhập giá trị cần xoá (từ tiếng Anh): ")
    del danh_sach_tu_dien[gia_tri_can_xoa]
    print()
    print("Danh sách từ điển sau khi đã xoá: ")
    print(danh_sach_tu_dien)
                
    print("\n=======================================\n")
    
    
tu_dien()