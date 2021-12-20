# Cho người dùng nhập số nguyên n và xuất các hình

# Câu a - số * theo biến n
def hinh_vuong(n):
    print("Hình vuông:")
    print(("* " * n + "\n")*n)

# Câu b - số * theo biến i
def tam_giac_vuong_thuong(n):
    print("Hình tam giác vuông thường:")
    for i in range(1, n + 1):
        print("*" * i)
    print()

# Câu c
def tam_giac_vuong_nguoc(n):
    print("Hình tam giác vuông ngược:")
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)
    print()

# Câu d
def tam_giac_deu_le(n):
    print("Hình tam giác đều (lẻ):")
    for i in range(1, n + 1, 2):
        print(("*" * i).center(n))
    print()

# Nhập và gọi hàm
n = int(input("Nhập n = "))
print()   
hinh_vuong(n)
tam_giac_vuong_thuong(n)
tam_giac_vuong_nguoc(n)
tam_giac_deu_le(n)