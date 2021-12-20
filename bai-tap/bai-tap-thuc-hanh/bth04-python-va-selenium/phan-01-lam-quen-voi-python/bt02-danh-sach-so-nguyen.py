# Viết chương trình cho phép người dùng
# nhập dãy n số nguyên khác 0,
# n (n > 0) nhập từ bán phím.

# Nhập danh sách

# region - Cách 1
def nhap_danh_sach(n):
    a = []
    for i in range(n):
        x = int(input("Nhập giá trị phần tử thứ %d = " % i))
        a.append(x)
    return a
# endregion

# region - Cách 2
def nhap_danh_sach_2(n):
    return [int(input("a[%d] = " % i)) for i in range(n)]
# endregion

print("\n=====================================\n")

n = int(input("Nhập n = "))
if n <= 0:
    exit()

a = nhap_danh_sach(n)
print("Mảng a =", a)

print("\n=====================================\n")

# Câu a: tìm số dương lớn nhất và số âm bé nhất

# region - Cách 1
mang_so_duong = []
for x in a:
    if x > 0:
        mang_so_duong.append(x)
# endregion

# region - Cách 2
mang_so_duong = [x for x in a if x > 0]
# endregion

print("Mảng =", a)

lon_nhat = max(a)
nho_nhat = min(a)

if lon_nhat < 0:
    print("Số dương lớn nhất: *")
else:
    print("Số dương lớn nhất:", lon_nhat)
    
if nho_nhat > 0:
    print("Số âm nhỏ nhất: *")
else:
    print("Số âm nhỏ nhất:", nho_nhat)

print("\n=====================================\n")

# Câu b: hiển thị tần số xuất hiện
#           của từng phần tử trong danh sách
for x in set(a):
    print("Số %d xuất hiện %d lần" % (x, a.count(x)))

print("\n=====================================\n")

# Câu c: hiển thị các phần tử trong danh sách
#           xuất hiện k lần, k nhập từ bàn phím
k = int(input("Nhập số cần đếm tần suất xuất hiện = "))
kq = []
for x in set(a):
    t = a.count(x)
    if t == k:
        kq.append(x)
    
print("Các phần tử xuất hiện %d lần là %s" % (k, str(kq)))

print("\n=====================================\n")

# Câu d: Sắp xếp danh sách giảm dần
a.sort(reverse=True)
print("Mảng được sắp xếp theo tứ tự giảm dần: ", a, "\n")