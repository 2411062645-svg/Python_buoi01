# ==========================================
# HOẠT ĐỘNG 1: DICTIONARY CƠ BẢN
# ==========================================
# Bài tập 1.1: Khai báo & truy xuất
sinh_vien = {
    "ho_ten": "Nguyen Van A",
    "nam_sinh": 2004,
    "diem_tb": 8.5
}

print("Họ tên:", sinh_vien["ho_ten"])
print("Điểm TB:", sinh_vien.get("diem_tb"))
print("Lớp:", sinh_vien.get("lop", "Chua co"))

# Giải thích câu hỏi lý thuyết Bài 1.1:
# - sinh_vien["lop"]: Gây lỗi KeyError vì khóa "lop" chưa tồn tại trong dictionary.
# - sinh_vien.get("lop", "Chua co"): Không báo lỗi vì phương thức get() trả về giá trị mặc định ("Chua co") khi không tìm thấy khóa.

# Bài tập 1.2: Thêm/sửa/xóa
sinh_vien["lop"] = "CNTT01"
sinh_vien["diem_tb"] = 9.0
print("Sau khi thêm lớp và sửa điểm:", sinh_vien)

diem_cu = sinh_vien.pop("diem_tb")
print("Sau khi xóa diem_tb:", sinh_vien, "- diem da xoa:", diem_cu)

sinh_vien.update({"nam_sinh": 2003, "email": "a@example.com"})
print("Sau khi update():", sinh_vien)

# ==========================================
# HOẠT ĐỘNG 2: DUYỆT DICTIONARY BẰNG FOR
# ==========================================
diem_mon_hoc = {"Toan": 8.0, "Ly": 7.5, "Hoa": 9.0, "Van": 6.5}

for mon in diem_mon_hoc.keys():
    print(mon)

for diem in diem_mon_hoc.values():
    print(diem)

for mon, diem in diem_mon_hoc.items():
    print(f"{mon}: {diem}")

tong_diem = 0
for diem in diem_mon_hoc.values():
    tong_diem = tong_diem + diem

print("Diem trung binh:", round(tong_diem / len(diem_mon_hoc), 2))

# ==========================================
# HOẠT ĐỘNG 3: COMPREHENSION & SET
# ==========================================
# Bài tập 3.1
diem_cong_diem = {mon: round(diem + 0.5, 2) for mon, diem in diem_mon_hoc.items()}
print(diem_cong_diem)

ten_mon_viet_hoa = {mon.upper(): diem for mon, diem in diem_mon_hoc.items()}
print(ten_mon_viet_hoa)

# Bài tập 3.2
mon_hoc_ky1 = {"Toan", "Ly", "Hoa", "Van"}
mon_hoc_ky2 = {"Toan", "Anh", "Tin", "Van"}

print("Giao (môn chung 2 kỳ):", mon_hoc_ky1 & mon_hoc_ky2)
print("Hợp (tất cả môn cả 2 kỳ):", mon_hoc_ky1 | mon_hoc_ky2)
print("Hiệu (môn chỉ có ở kỳ 1):", mon_hoc_ky1 - mon_hoc_ky2)

# Trả lời câu hỏi lý thuyết Bài 3.2:
# - Set không lưu cặp khóa-giá trị, Set chỉ lưu một tập hợp các giá trị đơn lẻ.
# - Set không cho phép phần tử trùng lặp vì nó sử dụng cơ chế Bảng băm (Hash Table) để đảm bảo tính duy nhất của từng phần tử.