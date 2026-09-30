# HOẠT ĐỘNG 4: PHẠM VI BIẾN – LOCAL, GLOBAL, TỪ KHÓA GLOBAL

so_luot_truy_cap = 0  # biến global

def tang_luot_truy_cap():
    global so_luot_truy_cap
    so_luot_truy_cap += 1

def vi_du_bien_local():
    so_luot_truy_cap = 100  # biến LOCAL
    print("Bên trong hàm, biến local =", so_luot_truy_cap)

print("--- Hoạt động 4 ---")
tang_luot_truy_cap()
tang_luot_truy_cap()
print("Số lượt truy cập (global):", so_luot_truy_cap)

vi_du_bien_local()
print("Sau khi gọi hàm, biến global vẫn là:", so_luot_truy_cap)


# HOẠT ĐỘNG 5: HÀM LAMBDA KẾT HỢP MAP(), FILTER(), SORTED()

danh_sach_so = [1, 2, 3, 4, 5]

# Bài tập 5.1 - map()
binh_phuong = list(map(lambda x: x ** 2, danh_sach_so))
print("\n--- Hoạt động 5 ---")
print("Bình phương:", binh_phuong)

# Bài tập 5.2 - filter()
so_chan = list(filter(lambda x: x % 2 == 0, danh_sach_so))
print("Số chẵn:", so_chan)

# Bài tập 5.3 - sorted()
danh_sach_sv = [
    {"ten": "An", "diem": 8.5},
    {"ten": "Bình", "diem": 7.0},
    {"ten": "Chi", "diem": 9.2},
]

sap_xep_theo_diem = sorted(danh_sach_sv, key=lambda sv: sv["diem"])
sap_xep_giam_dan = sorted(danh_sach_sv, key=lambda sv: sv["diem"], reverse=True)

print("\n--- Tăng dần ---")
for sv in sap_xep_theo_diem:
    print(sv["ten"], "-", sv["diem"])

print("\n--- Giảm dần ---")
for sv in sap_xep_giam_dan:
    print(sv["ten"], "-", sv["diem"])