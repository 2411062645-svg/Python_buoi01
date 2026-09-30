# HOẠT ĐỘNG 1: HÀM CƠ BẢN - DEF, THAM SỐ, RETURN

def uscln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def bscnn(a, b):
    return a * b // uscln(a, b)

def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def kiem_tra_so_hoan_thien(n):
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n

print("--- Hoạt động 1 ---")
print("USCLN(24, 36):", uscln(24, 36))
print("BSCNN(4, 6):", bscnn(4, 6))
print("Kiem tra nguyen to (29):", kiem_tra_nguyen_to(29))
print("Kiem tra so hoan thien (28):", kiem_tra_so_hoan_thien(28))


# HOẠT ĐỘNG 2: THAM SỐ MẶC ĐỊNH & THAM SỐ TỪ KHÓA

def in_loi_chao(ten):
    print(f"Xin chào, {ten}!")
    return  # hàm không trả về giá trị (trả về None)

def chia_lay_thuong_du(a, b):
    return a // b, a % b  # trả về nhiều giá trị qua tuple

def gioi_thieu(ten, tuoi=18, lop="Chưa rõ"):
    print(f"Tên: {ten} - Tuổi: {tuoi} - Lớp: {lop}")

print("\n--- Hoạt động 2 ---")
in_loi_chao("An")
thuong, du = chia_lay_thuong_du(17, 5)
print(f"Thương: {thuong}, Dư: {du}")

gioi_thieu("An")
gioi_thieu("Bình", 20)
gioi_thieu("Chi", lop="CNTT01")
gioi_thieu(ten="Dũng", lop="CNTT02", tuoi=19)


# HOẠT ĐỘNG 3: THAM SỐ LINH HOẠT - *ARGS VÀ **KWARGS

def tinh_tong(*args):
    tong = 0
    for so in args:
        tong += so
    return tong

def in_thong_tin(ho_ten, tuoi, **kwargs):
    print(f"\nHọ tên: {ho_ten} - Tuổi: {tuoi}")
    for khoa, gia_tri in kwargs.items():
        print(f"  {khoa}: {gia_tri}")

print("\n--- Hoạt động 3 ---")
print("Tổng 1, 2, 3:", tinh_tong(1, 2, 3))
print("Tổng 5, 10, 15, 20, 25:", tinh_tong(5, 10, 15, 20, 25))
print("Tổng rỗng:", tinh_tong())

in_thong_tin("Nguyễn Văn A", 20, lop="CNTT01", que_quan="Hà Nội")
in_thong_tin("Trần Thị B", 21, email="b@example.com")