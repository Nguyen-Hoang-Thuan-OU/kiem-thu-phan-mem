'''
Viết chương trình để kiểm tra tính hợp lệ
của mật khẩu mà người dùng nhập vào.

Các tiêu chí kiểm tra mật khẩu bao gồm:
1. Ít nhất 1 chữ cái nằm trong [a-z]
2. Ít nhất 1 số nằm trong [0-9]
3. Ít nhất 1 kí tự nằm trong [A-Z]
4. Ít nhất 1 ký tự nằm trong [$ # @]
5. Độ dài mật khẩu tối thiểu: 6
6. Độ dài mật khẩu tối đa: 12

Chương trình phải chấp nhận một chuỗi mật khẩu
phân tách nhau bởi dấu phẩy và kiểm tra xem chúng
có đáp ứng những tiêu chí trên hay không.

Mật khẩu hợp lệ sẽ được in,
mỗi mật khẩu cách nhau bởi dấu phẩy.

Ví dụ mật khẩu nhập vào chương trình là:
ABd1234@1,a F1#,2w3E*,2We3345
Thì đầu ra sẽ là: ABd1234@1
'''

import re

class BaiTapVeChuoi:
    def bt06(self):
        chuoi_nhap_vao =\
            input("Nhập vào danh sách chuỗi và phân tách nhau bởi dấu phẩy: ")
        
        # Tách chuỗi theo dấu phẩy
        danh_sach_chuoi = chuoi_nhap_vao.split(',')
        
        mat_khau = []
        
        # Duyệt từng phần tử và kiểm tra điều kiện
        for i in danh_sach_chuoi:
            
            # Độ dài mật khẩu tối thiểu và tối đa
            if len(i) > 6 and len(i) < 12:
                
                # Ít nhất 1 chữ cái nằm trong [a-z]
                if re.search("[a-z]", i):
                    
                    # Ít nhất 1 số nằm trong [0-9]
                    if re.search("[0-9]", i):
                        
                        # Ít nhất 1 kí tự nằm trong [A-Z]
                        if re.search("[A-Z]", i):
                            
                            # Ít nhất 1 ký tự nằm trong [$ # @]
                            if re.search("[$#@]", i):
                                mat_khau.append(i)
        
        print(mat_khau)
                
print("\n=====================================\n")

kiem_tra_mat_khau = BaiTapVeChuoi()
kiem_tra_mat_khau.bt06()

print("\n=====================================\n")