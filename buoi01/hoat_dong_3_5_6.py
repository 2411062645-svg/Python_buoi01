# ==========================================
# HOẠT ĐỘNG 3: ĐỊNH DANH & CHUẨN PEP8
# ==========================================
print("=== HOẠT ĐỘNG 3 ===")
ho_ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000

print("Họ và tên:", ho_ten)
print("Điểm Toán:", diem_toan)
print("Điểm Văn:", diem_van)
print("Số lượng môn học:", so_luong_mon_hoc)
print("Mức lương tối thiểu:", MUC_LUONG_TOI_THIEU)


# ==========================================
# HOẠT ĐỘNG 5: TOÁN TỬ
# ==========================================
print("\n=== HOẠT ĐỘNG 5 ===")
a, b = 17, 5
print("Toán tử số học:", a + b, a - b, a * b, a / b, a // b, a % b, a ** b)

diem, tuoi = 6.5, 20
print("Điểm Khá?:", (diem >= 6.5) and (diem < 8.0))
print("Tuổi < 18 hoặc > 60?:", (tuoi < 18) or (tuoi > 60))

x = 10
x += 5; x -= 3; x *= 2; x /= 4; x //= 2; x **= 3
print("x sau các phép gán:", x)
print("3 in list?:", 3 in [1, 2, 3, "python"])

print("Ưu tiên toán tử 1:", 2 + 3 * 4 ** 2)
print("Ưu tiên toán tử 2:", (2 + 3) * 4 ** 2)
print("Ưu tiên toán tử 3:", 10 > 5 and 3 < 1 or not False)


# ==========================================
# HOẠT ĐỘNG 6: BIẾN & DYNAMIC TYPING
# ==========================================
print("\n=== HOẠT ĐỘNG 6 ===")
bien = 10; print(bien, type(bien))
bien = "Xin chao"; print(bien, type(bien))
bien = 3.14; print(bien, type(bien))
bien = True; print(bien, type(bien))

dtb = (8.0 + 7.5 + 9.0) / 3
la_gioi = dtb >= 8.0
print("DTB:", round(dtb, 2), "- Đạt loại Giỏi?:", la_gioi)
print("Kiểu dữ liệu la_gioi:", type(la_gioi))